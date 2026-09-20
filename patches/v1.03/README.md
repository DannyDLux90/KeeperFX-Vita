# KeeperFX Vita: native display, controls and LAN networking

This update targets the Vita's native **960×544** panel.  The game keeps its
8-bit PAL framebuffer, but it is allocated and presented at 960×544 instead of
being forced through the old 640×480 mode.  Pointer coordinates are converted
between the touch/stick space and the active engine surface, so the whole
screen remains selectable.

## Controls

| Vita input | KeeperFX action |
| --- | --- |
| Front touch | Move pointer; tap selects; hold/drag keeps left button down |
| Two front fingers | Right mouse button |
| Right stick | Move pointer |
| L1 + right stick | Slow pointer for creature selection |
| Cross / Circle | Left / right mouse button |
| Left stick | Scroll the map camera |
| D-pad | Camera movement |
| L1 + D-pad up/down | Mouse wheel |
| Square / Triangle | Space / Tab |
| R1 | Left Ctrl |
| Start | Pause/options menu (Escape) |
| Select | Map (M) |

The native input layer is polled once per frame.  Vita IME dialogs temporarily
isolate game input and require a release before gameplay input resumes; this
prevents a held Start/Cross button from activating a menu after the dialog
closes.

## Pause and quit behavior

Start opens the options pause menu even while the player input lock is active.
The menu is processed while paused, and the local-player quit path now stops
the network service and sets the normal `quit_game`/`exit_keeper` flags.  This
avoids the previous black screen when selecting **Spiel beenden**.

## Vita-to-PC multiplayer

Vita builds keep KeeperFX networking enabled and use ENet 6.1.3 over native
SceNet IPv4 sockets.  The protocol is unchanged, so a PC KeeperFX build can
host or join the same LAN/direct-IP game.  In the Vita network screen, choose
LAN and use the Add button to enter `192.168.1.10` or `192.168.1.10:5555` in the
Vita keyboard.  The default ENet port is used when no port is supplied.  Online
matchmaking, STUN and automatic port forwarding remain disabled on Vita; they
are not needed for a local network or a manually forwarded IPv4 port.

The ENet transport sources are vendored in `deps/enet6` and the CMake Vita
target links them with `SceNet_stub` and `SceNetCtl_stub`.

## Validation and build notes

The host-side Vita input harness is in `tests/vita/test_input.c` and covers
native coordinates, precision mode, touch clicks, IME isolation and IPv4 input
validation.  The attached SDK snapshot does not include SDL2's CMake package
or the complete vitaGL/vitashark build dependencies, so a complete `.vpk`
rebuild and hardware run still require the normal VitaSDK/vdpm environment.
