# KeeperFX Vita v1.02 — exact status

This document describes the **hardware-tested state**, not planned features.

## Hardware-tested working state

The current stable public baseline is **v1.02**, derived from the previously confirmed v1.01 performance/rear-touch baseline.

Verified on a real PS Vita:

- Application starts normally.
- Campaign gameplay works.
- Level 2 performance is good and the previous ~1 FPS / severe stutter regression is fixed.
- The transferred-creature guard accepts only valid creature models **1..36** in the currently tested data set and rejects model 0 / corrupt transfer entries.
- Vita system language selection works. With the Vita set to German, KeeperFX menus/campaign selection use German and the original campaign audio is loaded from `campgns/keeporig_ger/`.
- Rear touch pad is disabled.
- Front touch remains active.
- Cross behaves as left mouse click / confirm.
- Circle behaves as right mouse click.
- The local 40-turn packet-history workaround remains active with networking disabled, preserving local world/camera controls.
- The Vita logger crash path through the unavailable `sceClibPrintf` route is bypassed in the stable binary.

## Known broken behavior

### In-game Quit / `Spiel beenden`

**Still broken in v1.02.**

Observed behavior from the hardware log after confirming the in-game quit dialog:

- the local player's allocated flag becomes zero;
- `view_type` / `view_mode` transition to zero;
- the gameplay loop keeps running instead of returning cleanly to the frontend.

Several experimental quit helpers were tried and rejected. They are **not considered fixed** and are not the basis of the public stable build.

Workaround: exit KeeperFX through the PS Vita system UI and restart the application.

### Source-only reproducibility

The current hardware-tested v1.02 program is based on the Vita source tree plus a small number of validated post-link/VELF changes. The exact binary is therefore **not yet reproduced by one clean source-only build**.

This is a known technical debt item. The intended final state is to move the verified language/performance/input fixes into normal source code and link them with vitaSDK without post-link patching.

## Performance fix details

The important transferred-creature validation used by the stable binary is equivalent to:

```text
model = transferred_creature.model
if ((unsigned)(model - 1) > 35)
    skip transfer
```

That accepts only models 1..36 and rejects model 0 and corrupted large values. The final clean source version should not hard-code 36; it should validate against KeeperFX's runtime creature model count.

## Language state

v1.02 maps the PS Vita system language to KeeperFX before language-dependent resources are selected. German has been verified on hardware.

The target mapping includes Japanese, English, French, Spanish, German, Italian, Dutch, Portuguese, Russian, Korean, Traditional/Simplified Chinese, Swedish, Danish, Norwegian and Polish where KeeperFX has corresponding language support. Unsupported Vita languages fall back to English.

## Networking state

Networking is disabled in this stable build. The goal is Vita ↔ PC multiplayer on the same WLAN using LAN discovery and/or direct IPv4 entry. See `NETWORK.md` for the unfinished probe state.

## Version history policy

Development experiments after the stable v1.01 baseline were discarded. The current release line is intentionally numbered **v1.02**.

Only behavior confirmed on physical hardware is described as working in this document.
