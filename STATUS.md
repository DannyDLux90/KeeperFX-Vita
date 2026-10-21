# KeeperFX Vita v1.03 — hardware acceptance status

## Current working baseline

**Version:** 1.03 (Controller RC4)  
**PS Vita title ID:** `KFXV00001`  
**VPK SHA-256:** `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d`  
**Real-hardware result:** user confirmed “v1.03 is finished and working as intended.”

### Confirmed functionality

- PS Vita boots the game and can start level 4; the previously recurring 100% load crash has been fixed.
- Root cause of the level crash: minimap colour table allowed only 16 background colours and wrote beyond the array. Final source allocates sufficient space for detected colours (28 seen in the hardware log).
- Native 960×544 display, frontend, land-view and gameplay.
- Native KVF intro audio with four-frame (~228 ms) preroll; tester confirmed audible distortion removed.
- World-map narration, including German map speech.
- Final RC4 input: L/R sidebar tab switching, D-pad target navigation, visible focus highlight, X confirmation, direct creature-portrait selection.
- Front touch, analog sticks and gameplay input remain supported; system language mapping retained.

### Not part of this acceptance statement

- LAN / Ad-Hoc multiplayer source work has **not** been fully exercised in the final 1.03 hardware run.
- Quit-to-main-menu had a known v1.02 problem. Later source contains quit-path changes, but the final RC4 test did not explicitly verify that case. Please report any regression.
- Developer recorder/dual-Start LiveArea prototype and experimental FFmpeg replacement video renderer are excluded from RC4.

### Release provenance

The v1.03 VPK equals the tested RC4 binary byte-for-byte. The complete final source snapshot differs from the initial September 2026 v1.03 sources in six C/C++ files and is delivered as a separate ZIP together with a workspace archive.

See [CHANGELOG-v1.03.md](CHANGELOG-v1.03.md), [RELEASE-v1.03.md](RELEASE-v1.03.md), [SOURCES.md](SOURCES.md) and [NETWORK.md](NETWORK.md). No commercial Dungeon Keeper assets are distributed.
