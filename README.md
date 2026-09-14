# KeeperFX Vita

Unofficial PlayStation Vita port / hardware-test branch of [KeeperFX](https://github.com/dkfans/keeperfx).

> **Current public status: v1.02 (hardware tested on a real PS Vita)**
>
> This repository intentionally does **not** contain commercial Dungeon Keeper game data.

## What currently works

- KeeperFX boots and is playable on PS Vita.
- Very good in-game performance on the tested campaign levels.
- Fix for corrupted transferred-creature records that previously caused severe Level 2 stutter.
- PS Vita system language is applied automatically to KeeperFX. German has been verified on hardware.
- German campaign speech/audio is selected correctly when the Vita system language is German.
- Cross = left mouse click / confirm.
- Circle = right mouse click.
- Front touch works as pointer/touch input.
- Rear touch pad is disabled.
- Local packet history is kept even with networking disabled, so camera/world controls work correctly.
- LiveArea / bubble assets use the known-good integrated Vita assets.

## Known issues

- **In-game `Spiel beenden` / Quit to main menu is still broken.** The quit action clears the local player state, but the gameplay loop does not reliably terminate and return to the frontend. Workaround: close the application with the PS Vita system UI and restart it.
- Multiplayer/networking is **not enabled in the stable v1.02 build**. LAN/direct-IP work exists only as an unfinished probe; see `NETWORK.md`.
- The exact hardware-tested v1.02 binary still contains a few validated post-link/VELF patches. A fully clean source-only rebuild that reproduces the exact public binary is still TODO; see `STATUS.md`.
- Some non-fatal configuration warnings from the current KeeperFX data set may appear in `keeperfx.log`.

## Installing

1. Install the public VPK with VitaShell.
2. Provide your own legal Dungeon Keeper data and KeeperFX data under `ux0:data/keeperfx/`.
3. Start KeeperFX from LiveArea.

Full instructions: **[INSTALL.md](INSTALL.md)**.

The public VPK contains only a tiny license-free placeholder data archive because the current first-run bootstrap expects `app0:/game_data/keeperfx_data_bundle.zip`. It contains **no game assets**.

## Screenshots
<img width="960" height="544" alt="2026-09-14-123237" src="https://github.com/user-attachments/assets/b990edd4-7b3a-489e-901c-8aebc4f5e134" />
<img width="960" height="544" alt="2026-09-14-123145" src="https://github.com/user-attachments/assets/f2221dd3-8465-4b61-8cbc-cf60d1c4ab1f" />
<img width="960" height="544" alt="2026-09-14-123128" src="https://github.com/user-attachments/assets/fbb4e306-596b-49c7-873d-c0202461c7df" />
<img width="960" height="544" alt="2026-09-14-123112" src="https://github.com/user-attachments/assets/0e7e54c6-3f70-4229-9cd9-7d5c7e46690b" />


## Release files

Recommended public release name:

`KeeperFX-Vita-v1.02-PUBLIC-no-game-data.vpk`

Do **not** publicly distribute the private integrated VPK because that package contains user-supplied game data.

## Project status / TODO

See **[STATUS.md](STATUS.md)** for the exact hardware-tested state and **[NETWORK.md](NETWORK.md)** for the multiplayer roadmap.

## Upstream and sources

The port is based on KeeperFX and the Vita homebrew toolchain/ecosystem. Exact references and the pinned upstream commit are documented in **[SOURCES.md](SOURCES.md)**.

KeeperFX upstream base used for this development line:

`dkfans/keeperfx @ 466e0753e17cee876f2ace6fa6b1e17f3ad44b0d`

## License

KeeperFX is GPL-2.0 licensed. This repository carries the corresponding GPL-2.0 license for source modifications. Commercial Dungeon Keeper assets are not part of this repository or the public VPK.
