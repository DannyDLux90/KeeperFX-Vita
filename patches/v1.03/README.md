# v1.03 final source state

The hardware-tested final v1.03 was built from the original 2026-09-20 Vita v1.03 source snapshot, with six source files changed:

- `src/front_input.c`
- `src/bflib_fmvids.cpp`
- `src/frontmenu_ingame_map.c`
- `src/frontend.cpp`
- `src/audio/audio_vita.c`
- `src/input/input_vita.c`

The matching source and workspace ZIP archives and a six-file unified patch were generated for the release. The source ZIP contains the full project tree. See [release notes](../../RELEASE-v1.03.md) and [changelog](../../CHANGELOG-v1.03.md).

The final file hashes can be checked against the shipped RC4 VPK: `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d` (SHA-256). The published source ZIP and workspace ZIP were integrity-tested before handoff.

This documentation repository does not contain the binary source/workspace ZIP archives. Do not upload user-supplied Dungeon Keeper game assets.

The experimental FFmpeg replacement player, 640×480 intro switch and two-button LiveArea recorder builds are **not** release features.
