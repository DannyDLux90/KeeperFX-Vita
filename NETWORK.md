# Networking / Multiplayer status

Networking is **not part of the stable v1.02 public build**.

The target is straightforward local multiplayer between:

- PS Vita ↔ PC on the same WLAN;
- preferably LAN discovery where practical;
- direct IPv4 entry as a fallback.

## What has already been explored

An experimental Vita networking probe was prepared that:

- enables `KEEPERFX_NETWORKING` on Vita;
- keeps online matchmaking disabled;
- keeps the existing KeeperFX ENet6 LAN/gameplay networking sources;
- links Vita network libraries (`SceNet`, `SceNetCtl`, `SceSysmodule`);
- initializes the Vita network subsystem before KeeperFX creates ENet hosts;
- replaces desktop-only NAT-PMP/UPnP and curl/WebSocket matchmaking with Vita probe stubs.

The patch is kept in:

```text
patches/post-v14/patch_network_probe.py
```

## What is still missing

This probe is **unfinished and not hardware-certified**. It is not shipped in v1.02.

The main remaining work is:

1. Verify Vita ↔ PC LAN discovery and session joining on real hardware.
2. Finish the direct-IP frontend path.
3. Add a native PS Vita IME dialog for entering an IPv4 address.
4. Prefill the IME with the current value, accept only digits and `.` where possible, safely copy on OK, and keep the old value on Cancel.
5. Validate connect/disconnect, host/join, level transitions and repeated sessions.
6. Confirm that enabling networking does not regress the local packet-history/camera fixes or performance.

## Online matchmaking / NAT traversal

Not a current target for the first working Vita multiplayer release.

The current plan is to get same-WLAN LAN/direct-IP multiplayer stable first. Automatic router mapping and internet matchmaking can be considered separately later.

## Important

Do not interpret the presence of the networking probe source as proof that multiplayer works. The stable public v1.02 build keeps networking disabled.
