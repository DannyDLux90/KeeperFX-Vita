# Installation — KeeperFX Vita v1.02

The public VPK intentionally contains **no commercial Dungeon Keeper game data**.

## Requirements

- A PS Vita / PS TV capable of running homebrew.
- VitaShell (or an equivalent VPK/file manager).
- The public KeeperFX Vita v1.02 VPK.
- A legal copy of **Dungeon Keeper** (for example GOG or CD).
- KeeperFX release data compatible with this development line.

## 1. Install the public VPK

Copy the VPK to the Vita and install it with VitaShell.

Recommended public filename:

```text
KeeperFX-Vita-v1.02-PUBLIC-no-game-data.vpk
```

The application installs as **KeeperFX** with title ID:

```text
KFXV00001
```

## 2. Create the data directory

All runtime data is read from:

```text
ux0:data/keeperfx/
```

Create the directory if it does not exist.

## 3. Copy KeeperFX data

Copy the KeeperFX data directories into `ux0:data/keeperfx/`.

Typical layout:

```text
ux0:data/keeperfx/
├── keeperfx.cfg
├── data/
├── fxdata/
├── hdata/
├── campgns/
├── config/
├── lang/
├── levels/
├── creatrs/
├── music/
├── sound/
└── ...
```

Use the data from a KeeperFX release/source setup compatible with the pinned upstream base documented in `SOURCES.md`.

## 4. Copy your own original Dungeon Keeper data

From your legally owned Dungeon Keeper installation, copy the original game assets into the same `ux0:data/keeperfx/` tree.

Important original data includes the contents normally found under Dungeon Keeper's `data/` and `sound/` directories, such as `.dat`, `.pal`, `.tab`, `.raw`, `.col` and the original audio resources.

For GOG installations, tools such as `innoextract` can be used on a PC to extract the installer without installing the Windows game first.

**Do not upload or redistribute those commercial files with the public VPK.**

## 5. Configuration

A minimal configuration should include:

```ini
INSTALL_PATH .
```

The v1.02 Vita build automatically selects the KeeperFX language from the PS Vita system language. German has been verified on hardware, so manually forcing `LANGUAGE GER` is not required for the current build.

If an existing `keeperfx.cfg` already contains a `LANGUAGE` line, v1.02 still applies the Vita system-language selection during startup.

## Important first-start note

The current Vita bootstrap expects this application-side file to exist:

```text
app0:/game_data/keeperfx_data_bundle.zip
```

The **public VPK includes a tiny license-free placeholder archive only**. It contains no Dungeon Keeper assets. On first launch it lets the bootstrap complete its normal marker/install step.

For the best first-run experience, copy your real data to `ux0:data/keeperfx/` **before launching KeeperFX for the first time**.

If you accidentally launch it before copying the data, simply exit, copy the required files, and launch again.

## Logs

Useful diagnostic files are written to:

```text
ux0:data/keeperfx/keeperfx.log
ux0:data/keeperfx/kfx_boot.log
ux0:data/keeperfx/kfx_preinit.log
ux0:data/keeperfx/profiler.log
ux0:data/keeperfx/vita_install.log
```

If reporting a bug, include the most recent versions of these files.

## Updating an existing installation

Installing a newer VPK with the same title ID normally updates the application while leaving `ux0:data/keeperfx/` intact.

Keep a backup of your saves/configuration before testing development builds.

## Current known issue

The in-game menu action **`Spiel beenden` / Quit game** still does not return reliably to the main menu. Until this is fixed, use the PS Vita system UI to close KeeperFX when you want to leave a running level.
