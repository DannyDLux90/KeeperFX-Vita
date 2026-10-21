# KeeperFX Vita — Changelog v1.02 → v1.03

Release date: 2026-10-21  
Base project: KeeperFX (upstream version string 1.3.2.0)  
PS Vita application ID: `KFXV00001`

## Gameplay, stability and rendering

- Native **960 × 544** PAL8 gameplay/frontend presentation using vitaGL and a precompiled palette shader; the Vita output no longer needs the old 640 × 480 internal gameplay mode.
- Reworked Vita frontend/software-UI sprite registration and GUI scaling, including the approximately 193-pixel-wide ingame sidebar.
- Fixed the ingame crash caused by the **minimap background-colour table overflowing its original 16-colour capacity**. The table now grows to the required count (28 colours were observed during the hardware test).
- Improved framebuffer/pointer coordinate handling and land-view presentation performance. The world-map background is cached while stationary, and unchanged palette uploads can be skipped.
- Retained the functioning native Vita renderer and disabled runtime GPU shader paths that caused crashes in development builds.

## Audio and movies

- Retained the native **KVF** intro player with original colour palettes and normal movie timing. Legally sourced SMK videos are converted into adjacent lossless KVF caches outside the Vita.
- Fixed audible intro distortion by **preloading four KVF frames (~228 ms of audio) before playback**, keeping original 48 kHz stereo PCM content unchanged.
- Kept the working double-buffered Vita audio output for **German map narration** and FFmpeg-backed MP3 decoding/prebuffering.
- The converted KVF audio samples are lossless; the experimental FFmpeg replacement video player was not included in the final release.

## Controller and touch input

- **L/R** cycle through five ingame sidebar tabs: Information, Rooms, Spells, Traps/Doors and Creatures.
- **D-pad** navigates enabled sidebar controls; **X/Cross** triggers the selected control through the normal GUI click path.
- Added a high-contrast yellow focus outline with a dark edge so the active sidebar item is visible.
- The creature menu navigates **directly to creature portraits** rather than activity filters; portrait selection uses the original creature click callbacks.
- Corrected Vita shoulder-button masks to `SCE_CTRL_LTRIGGER` / `SCE_CTRL_RTRIGGER` (`0x100` / `0x200`) and portrait-owner check to `gmenu_idx`.
- Existing analog-stick, touchscreen, SELECT/map and Circle/right-click behaviour remains available.

## Additional Vita integration

- Original campaign map speech is selected using the Vita system language (German confirmed).
- Improvements to native IME text entry and local UI/controller interaction.
- Development-source LAN/Ad-Hoc discovery and direct-IP support is present, but **networking was not included in the final hardware acceptance test**.

## Hardware acceptance and packaging

- Final code matches **Controller RC4**, explicitly reported working by the PS Vita tester.
- Intro audio and level-start crash fixes were separately confirmed on a real Vita prior to RC4.
- Renderer stays at native **960 × 544**, with game and movie resources unchanged.
- Public VPK and source/workspace distributions exclude commercial Dungeon Keeper data.

## Not part of the final v1.03 release

- The experimental replacement FFmpeg KVF video player, 640 × 480 intro mode, and experimental video recorder/dual-start bubble are **not** part of the final RC4 build.
- Multiplayer/networking remains unverified for this final build.
- The historical v1.02 in-game quit-to-menu limitation has not been independently re-tested in the final RC4 acceptance run.

## Final LiveArea manual update (2026-10-21)

- Updated the in-bubble **Tasten & Sticks** page for the RC4 control scheme.
- Added a sixth manual page explaining L/R menu tabs, the visible yellow focus outline and direct creature-portrait selection with the D-pad and X.
- Kept existing touch, installation and troubleshooting help pages. All page numbers now show 1/6–6/6.
- Documentation-only VPK revision: exact RC4 `eboot.bin` retained. See [MANUAL-v1.03.md](MANUAL-v1.03.md).
