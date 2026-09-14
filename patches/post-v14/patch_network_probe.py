from pathlib import Path


def replace_once(text, old, new, name):
    if old not in text:
        raise SystemExit(f'network probe: pattern not found: {name}')
    return text.replace(old, new, 1)

# 1) Enable real networking on Vita, but keep online matchmaking out of the
# first probe. LAN/direct-IP does not need curl/WebSockets or NAT traversal.
p = Path('build/cmake/modules/Platforms.cmake')
s = p.read_text(encoding='utf-8')
old = '''option(KEEPERFX_NETWORKING "Build with multiplayer networking support" ON)\nif(PLATFORM_VITA OR PLATFORM_3DS OR PLATFORM_SWITCH OR PLATFORM_WII_U)\n    set(KEEPERFX_NETWORKING OFF CACHE BOOL "Networking disabled on homebrew" FORCE)\nendif()\n'''
new = '''option(KEEPERFX_NETWORKING "Build with multiplayer networking support" ON)\nif(PLATFORM_VITA)\n    set(KEEPERFX_NETWORKING ON CACHE BOOL "Vita LAN/direct-IP networking probe" FORCE)\n    set(KEEPERFX_MATCHMAKING OFF CACHE BOOL "Online matchmaking disabled for Vita LAN probe" FORCE)\nelseif(PLATFORM_3DS OR PLATFORM_SWITCH OR PLATFORM_WII_U)\n    set(KEEPERFX_NETWORKING OFF CACHE BOOL "Networking disabled on homebrew" FORCE)\nendif()\n'''
s = replace_once(s, old, new, 'Vita networking option')
p.write_text(s, encoding='utf-8')

# 2) Replace desktop-only NAT-PMP/UPnP and curl matchmaking with small Vita
# stubs. The actual ENet6/LAN/gameplay networking sources remain compiled.
stub = r'''/******************************************************************************
 * Vita LAN/direct-IP networking probe stubs.
 * Online matchmaking and automatic router mapping are deliberately omitted.
 ******************************************************************************/
#include "pre_inc.h"
#include "net_portforward.h"
#include "net_matchmaking.h"
#include "post_inc.h"

struct TbNetworkSessionNameEntry matchmaking_sessions[MATCHMAKING_SESSIONS_MAX];
int matchmaking_session_count = 0;
char join_lobby_id[MATCHMAKING_ID_MAX] = {0};

int port_forward_add_mapping(uint16_t port) { (void)port; return 0; }
void port_forward_remove_mapping(void) {}

void matchmaking_connect_async(void) {}
int matchmaking_connect(void) { return -1; }
int matchmaking_request_list(void) { return -1; }
void matchmaking_disconnect(void) {}
void matchmaking_refresh_sessions(void) { matchmaking_session_count = 0; }
int matchmaking_create(const char *name, int udp_ipv4_port, int udp_ipv6_port)
{ (void)name; (void)udp_ipv4_port; (void)udp_ipv6_port; return -1; }
int matchmaking_punch(const char *lobby_id, int udp_ipv4_port, int udp_ipv6_port, PunchAddresses *output)
{ (void)lobby_id; (void)udp_ipv4_port; (void)udp_ipv6_port; (void)output; return -1; }
int matchmaking_poll_punch(PunchAddresses *output) { (void)output; return -1; }
'''
Path('src/net_vita_probe_stubs.c').write_text(stub, encoding='utf-8')

p = Path('build/cmake/modules/BuildTargets.cmake')
s = p.read_text(encoding='utf-8')
anchor = '''if(NOT KEEPERFX_MATCHMAKING)\n    list(FILTER KEEPERFX_SOURCES_C EXCLUDE REGEX ".*/net_matchmaking\\\\.c$")\nendif()\n'''
if anchor not in s:
    anchor = '''if(NOT KEEPERFX_MATCHMAKING)\n    list(FILTER KEEPERFX_SOURCES_C EXCLUDE REGEX ".*/net_matchmaking\\.c$")\nendif()\n'''
extra = anchor + '''\nif(PLATFORM_VITA AND KEEPERFX_NETWORKING)\n    # miniupnpc/libnatpmp and curl-WebSocket matchmaking are desktop-only in\n    # this first Vita probe. Keep the actual ENet6 LAN/gameplay stack.\n    list(FILTER KEEPERFX_SOURCES_CXX EXCLUDE REGEX ".*/net_portforward\\\\.cpp$")\n    list(FILTER KEEPERFX_SOURCES_C EXCLUDE REGEX ".*/net_matchmaking\\\\.c$")\n    list(APPEND KEEPERFX_SOURCES_C "src/net_vita_probe_stubs.c")\nendif()\n'''
if anchor not in s:
    raise SystemExit('network probe: matchmaking exclusion anchor not found')
s = s.replace(anchor, extra, 1)
p.write_text(s, encoding='utf-8')

# 3) Link ENet6 and Vita network libraries.
p = Path('build/cmake/modules/PlatformVita.cmake')
s = p.read_text(encoding='utf-8')
anchor = '''# Cortex-A9 NEON optimization\n'''
net_cmake = '''# Vita LAN/direct-IP networking probe\nif(KEEPERFX_NETWORKING)\n    find_library(ENET6_LIB enet6 HINTS "$ENV{VITASDK}/arm-vita-eabi/lib" REQUIRED)\n    find_path(ENET6_INCLUDE_DIR enet6/enet.h HINTS "$ENV{VITASDK}/arm-vita-eabi/include" REQUIRED)\n    foreach(_target IN LISTS KFX_TARGETS)\n        target_include_directories(${_target} PRIVATE ${ENET6_INCLUDE_DIR})\n        target_link_libraries(${_target} PRIVATE ${ENET6_LIB} SceNet_stub SceNetCtl_stub SceSysmodule_stub)\n    endforeach()\nendif()\n\n'''
s = replace_once(s, anchor, net_cmake + anchor, 'Vita ENet6 link block')
p.write_text(s, encoding='utf-8')

# 4) Bring up the Vita network subsystem before KeeperFX creates ENet hosts.
p = Path('src/platform/PlatformVita.cpp')
s = p.read_text(encoding='utf-8')
inc_anchor = '#include <psp2/rtc.h>\n'
inc_add = '''#include <psp2/rtc.h>\n#ifdef KEEPERFX_NETWORKING\n#include <psp2/sysmodule.h>\n#include <psp2/net/net.h>\n#include <psp2/net/netctl.h>\n#endif\n'''
s = replace_once(s, inc_anchor, inc_add, 'Vita network includes')
state_anchor = 'static bool s_vita_video_ready = false;\n'
state = r'''static bool s_vita_video_ready = false;
#ifdef KEEPERFX_NETWORKING
static void *s_vita_net_memory = NULL;
static bool s_vita_net_ready = false;

static void vita_network_shutdown(void)
{
    if (!s_vita_net_ready)
        return;
    sceNetCtlTerm();
    sceNetTerm();
    sceSysmoduleUnloadModule(SCE_SYSMODULE_NET);
    free(s_vita_net_memory);
    s_vita_net_memory = NULL;
    s_vita_net_ready = false;
}

static int vita_network_initialize(void)
{
    int rc = sceSysmoduleLoadModule(SCE_SYSMODULE_NET);
    if (rc < 0)
        return rc;

    const int net_mem_size = 1024 * 1024;
    s_vita_net_memory = malloc(net_mem_size);
    if (s_vita_net_memory == NULL) {
        sceSysmoduleUnloadModule(SCE_SYSMODULE_NET);
        return -1;
    }

    SceNetInitParam param;
    memset(&param, 0, sizeof(param));
    param.memory = s_vita_net_memory;
    param.size = net_mem_size;
    param.flags = 0;
    rc = sceNetInit(&param);
    if (rc < 0) {
        free(s_vita_net_memory);
        s_vita_net_memory = NULL;
        sceSysmoduleUnloadModule(SCE_SYSMODULE_NET);
        return rc;
    }

    rc = sceNetCtlInit();
    if (rc < 0) {
        sceNetTerm();
        free(s_vita_net_memory);
        s_vita_net_memory = NULL;
        sceSysmoduleUnloadModule(SCE_SYSMODULE_NET);
        return rc;
    }

    s_vita_net_ready = true;
    atexit(vita_network_shutdown);
    return 0;
}
#endif
'''
s = replace_once(s, state_anchor, state, 'Vita network state')
init_anchor = '''    _SYSI_LOG("clks-done");\n'''
init_code = '''    _SYSI_LOG("clks-done");\n#ifdef KEEPERFX_NETWORKING\n    {\n        int net_rc = vita_network_initialize();\n        FILE *netlog = fopen("ux0:data/keeperfx/kfx_boot.log", "a");\n        if (netlog) {\n            fprintf(netlog, "sysinit:network rc=0x%08X ready=%d\\n", (unsigned int)net_rc, s_vita_net_ready ? 1 : 0);\n            fclose(netlog);\n        }\n    }\n#endif\n'''
s = replace_once(s, init_anchor, init_code, 'Vita network init call')
p.write_text(s, encoding='utf-8')

checks = {
    'build/cmake/modules/Platforms.cmake': ['Vita LAN/direct-IP networking probe', 'KEEPERFX_NETWORKING ON', 'KEEPERFX_MATCHMAKING OFF'],
    'build/cmake/modules/PlatformVita.cmake': ['ENET6_LIB', 'SceNet_stub', 'SceNetCtl_stub', 'SceSysmodule_stub'],
    'src/platform/PlatformVita.cpp': ['vita_network_initialize', 'sceNetInit(&param)', 'sceNetCtlInit()', 'SCE_SYSMODULE_NET'],
    'src/net_vita_probe_stubs.c': ['port_forward_add_mapping', 'matchmaking_refresh_sessions'],
}
for name, needles in checks.items():
    text = Path(name).read_text(encoding='utf-8')
    for needle in needles:
        if needle not in text:
            raise SystemExit(f'network probe gate failed {name}: {needle}')

print('Vita LAN/direct-IP network probe patch applied')
