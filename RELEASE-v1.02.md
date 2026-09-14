# KeeperFX Vita v1.02 release notes

## Recommended public artifact

```text
KeeperFX-Vita-v1.02-PUBLIC-no-game-data.vpk
```

SHA256:

```text
ab5f2c1a93788c5edd66b31fa5332307106a6a85e36dd2a9e00d21eeeaf3b272
```

This is the file that may be uploaded publicly. It contains the v1.02 program, LiveArea/manual assets and a tiny license-free placeholder archive required by the current first-run bootstrap. It contains **no commercial Dungeon Keeper game assets**.

Users must follow `INSTALL.md` and provide their own legal game data under `ux0:data/keeperfx/`.

## Source/status snapshot

Recommended companion source archive:

```text
KeeperFX-Vita-v1.02-SOURCE-SNAPSHOT-no-game-data.zip
```

SHA256:

```text
9c586024262c5b6c9baf8e54318753b9ce58385fba96bc3e12dfb38c71be8896
```

This snapshot contains the retained Vita source baseline and the patch/post-link documentation used for the current development state. It contains no commercial game data.

## Private integrated artifact

A separate private convenience build exists for the project owner:

```text
KeeperFX-Vita-v1.02-PRIVATE-with-game-data.vpk
```

SHA256:

```text
484210e5ec1774d314c8d4179a9f75a4abb44713ad78811b2fd6d1020e6294e0
```

**Do not upload or redistribute the private VPK.** It contains the project owner's locally supplied game-data bundle.

## Hardware-tested status

- Boots and plays on real PS Vita hardware.
- Good performance; the severe Level 2 stutter caused by corrupted transferred-creature records is fixed.
- Vita system language works; German is hardware-verified.
- German original-campaign speech is selected correctly.
- Rear touch is disabled.
- Cross = left click; Circle = right click.
- In-game `Spiel beenden` / Quit-to-main-menu remains broken.
- Networking/multiplayer remains disabled in the stable build; an unfinished LAN/direct-IP probe is documented separately.

See `STATUS.md` for the exact technical state.

## Important release policy

Do not describe a feature as working unless it has been confirmed on physical hardware. Experimental quit/network patches are not release features.
