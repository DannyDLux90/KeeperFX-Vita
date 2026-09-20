# KeeperFX Vita 1.03 work-in-progress changes

This patch updates the attached Vita source snapshot for the native 960x544 display and expands input and LAN support.

## Included

- Native 960x544 PAL8 mode registration, video-mode availability reporting, pointer scaling and vitaGL presentation.
- Start/Escape pause-menu handling while paused, software UI reinitialization, and local quit cleanup so **Spiel beenden** exits instead of leaving a black screen.
- Front touch tap/drag and two-finger right click, right-stick pointer movement, left-stick camera movement, precision mode, wheel shortcuts and physical button mappings.
- Vita IME address entry and strict IPv4[:port] validation.
- ENet 6.1.3 vendored with a native SceNet IPv4 transport, keeping packet compatibility with the PC KeeperFX build.
- Vita LAN/direct-IP session support; cloud matchmaking/STUN/automatic port mapping remain disabled on the console.
- Host-side input regression harness in `tests/vita/test_input.c`.

## Validation

The host harness passes native input, precision, touch, IME isolation, coordinate mapping and IPv4 validation. Changed C/C++ Vita sources and ENet transport sources compile with the attached ARM Vita toolchain.

A complete VPK build and hardware run were not possible in this workspace because the attached SDK snapshot lacks SDL2's CMake package and the complete vitaGL/vitashark dependency set. The patch therefore needs the normal VitaSDK/vdpm environment for the final `.vpk` build and hardware verification.
