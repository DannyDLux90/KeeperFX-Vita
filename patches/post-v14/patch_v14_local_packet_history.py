from pathlib import Path

p = Path('src/bflib_network_stub.c')
s = p.read_text(encoding='utf-8')

if '#include <string.h>\n' not in s:
    s = s.replace('#include <stddef.h>\n', '#include <stddef.h>\n#include <string.h>\n', 1)

old = '''/* net_exchange_gameplay.c — packet history stubs */\nvoid initialize_packet_history(void) {}\nvoid store_packet_history(PlayerNumber player, const struct Packet *packet) { (void)player; (void)packet; }\nconst struct Packet *get_history_packet(PlayerNumber player, GameTurn turn) { (void)player; (void)turn; return NULL; }\nvoid process_gameplay_chat_message(int player_id, const char *message) { (void)player_id; (void)message; }\n'''
new = '''/* net_exchange_gameplay.c — local packet history.\n * KeeperFX uses packet history for local camera/input processing too.\n */\n#define LOCAL_PACKET_HISTORY_SIZE 40\nstruct LocalPacketHistory {\n    struct Packet entries[LOCAL_PACKET_HISTORY_SIZE];\n};\nstatic struct LocalPacketHistory s_local_packet_history[MAX_NET_USERS];\n\nvoid initialize_packet_history(void)\n{\n    memset(s_local_packet_history, 0, sizeof(s_local_packet_history));\n}\n\nvoid store_packet_history(PlayerNumber player, const struct Packet *packet)\n{\n    if (player < 0 || player >= MAX_NET_USERS || packet == NULL || is_packet_empty(packet))\n        return;\n    struct Packet *entry = &s_local_packet_history[player].entries[packet->turn % LOCAL_PACKET_HISTORY_SIZE];\n    if (!is_packet_empty(entry) && (GameTurnDelta)(entry->turn - packet->turn) > 0)\n        return;\n    *entry = *packet;\n}\n\nconst struct Packet *get_history_packet(PlayerNumber player, GameTurn turn)\n{\n    if (player < 0 || player >= MAX_NET_USERS)\n        return NULL;\n    const struct Packet *packet = &s_local_packet_history[player].entries[turn % LOCAL_PACKET_HISTORY_SIZE];\n    if (is_packet_empty(packet) || packet->turn != turn)\n        return NULL;\n    return packet;\n}\n\nvoid process_gameplay_chat_message(int player_id, const char *message) { (void)player_id; (void)message; }\n'''
if old not in s:
    raise SystemExit('v14 patch: packet history stub block not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
