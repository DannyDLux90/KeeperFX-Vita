# KeeperFX Vita

Unofficial PlayStation Vita port / hardware-test branch of [KeeperFX](https://github.com/dkfans/keeperfx).

> **Current public status: v1.03 — hardware tested on a real PS Vita (Controller RC4)**
>
> This repository intentionally contains **no commercial Dungeon Keeper game data**.

## v1.03 highlights

- Native **960 × 544** display (PAL8 software rendering + vitaGL precompiled palette shader).
- Fixed the level-start crash caused by the minimap's 16-background-colour allocation overflowing into GUI/camera data.
- Fixed distorted intro audio with **four KVF frames of audio preroll**, preserving the original lossless PCM data and native KVF video playback.
- German world-map MP3 narration works through the Vita audio output with double buffering.
- Improved PS Vita ingame controls: **L/R** cycle sidebar tabs, **D-pad** navigates buttons, **X/Cross** selects a highlighted item, including **creature portraits** directly. A yellow focus outline marks the currently selected item.
- Right analog stick, front touch and original map controls remain available.
- PS Vita system language selects available KeeperFX language/campaign audio (German confirmed).

Full changes: **[CHANGELOG-v1.03.md](CHANGELOG-v1.03.md)**.  
Final release notes and source/workspace package description: **[RELEASE-v1.03.md](RELEASE-v1.03.md)**.

## Installing and game data

1. Obtain the public `KeeperFX-Vita-v1.03-FINAL-no-game-data.vpk` build.
2. Install via VitaShell.
3. Provide your own legally acquired Dungeon Keeper and compatible KeeperFX data under `ux0:data/keeperfx/`.
4. Start KeeperFX from the existing LiveArea bubble (`KFXV00001`).

Full instructions: **[INSTALL.md](INSTALL.md)**.

The public VPK contains only the noncommercial bootstrap placeholder data archive. Do **not** redistribute an integrated private VPK containing proprietary game assets.

## What is verified and what is not

**Hardware-tested:** level starts and gameplay (including level 4), clean introductory audio, map speech and RC4 sidebar controls. Native 960×544 rendering is retained.

**Not independently re-tested during final RC4 acceptance:** quit-to-menu reliability and LAN/Ad-Hoc multiplayer. Networking source experiments are not a promise of supported release functionality. See [STATUS.md](STATUS.md) and [NETWORK.md](NETWORK.md).

**Not included:** the experimental FFmpeg replacement KVF video renderer, the 640×480 intro-mode experiment, or the two-start-button recorder/debug-bubble prototype.

## Source / workspace

The full final source tree and build workspace were prepared as companion release archives, without commercial game data. This repository maintains release docs, provenance, and patch notes rather than checking large binary workspaces into Git. See [SOURCES.md](SOURCES.md) and [RELEASE-v1.03.md](RELEASE-v1.03.md).

Upstream pinned base: `dkfans/keeperfx @ 466e0753e17cee876f2ace6fa6b1e17f3ad44b0d`.

## Licence

KeeperFX and the corresponding Vita source modifications use GPL-2.0. Third-party libraries retain their own licences. Commercial Dungeon Keeper assets are not included.
