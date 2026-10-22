# KeeperFX Vita 1.03 — Possession Speed V2 (hardware test candidate)

**Status: TEST BUILD ONLY.** The accepted 1.03 RC4 program and the updated LiveArea manual remain the stable baseline on the repository's `main` branch. No new release tag has been created.

## Reason for the change

The first Symbiose/possession controller fix stopped runaway rotation by feeding the right analog stick directly into the first-person packet with a deadzone. On PS Vita hardware the player then reported that looking around was **far too slow**.

Two separate limits caused this: the analog translation capped movement at 14 units, and `process_first_person_look()` capped turning to each creature's `max_turning_speed` (default 15). Merely raising the first limit would have little effect.

## Changes

- **`src/input/input_vita.c`**: maximum right-stick packet look vector increased from 14 to **48**, deadzone remains 30; neutral input still produces exactly 0. A unique boot log announces `Vita possession speed V2: deadzone=30, max=48, turn_cap=3x (TEST)`.
- **`src/front_input.c`**: possession first-use log updated; existing inversion and sensitivity settings are still applied, with normal dungeon pointer control unchanged.
- **`src/packets.c`**: only on Vita, when calculating first-person possession look, the maximum turn speed is tripled. Normal creature AI/movement settings are not modified. Effective full-stick turning for a creature with default cap 15 becomes 45 instead of about 14.
- **`tests/vita_possession_axis_regression.c`**: updated monotonicity, range, deadzone and effective-cap regression tests.

Patch against the earlier *Symbiose Controls* test source: [possession-speed-v2.patch](possession-speed-v2.patch).

## Build and artifact verification

- VitaSDK ARM compiler, link, Sony SELF conversion and VPK packaging completed successfully.
- Produced no-game-data test artifact: `KeeperFX-Vita-v1.03-POSSESSION-SPEED-V2-TEST-no-game-data.vpk`
- VPK SHA-256: `76ff91a028c8bf3e73931c4b56549c3a1180f8a0c679caec20a26746af45366e`
- Source archive: `KeeperFX-Vita-v1.03-POSSESSION-SPEED-V2-SOURCE-no-game-data.zip`, SHA-256 `c6205a0aa1674052de4d9b318e1e68c6d92a55d209411482ce72b23401aea587`
- Workspace archive: `KeeperFX-Vita-v1.03-POSSESSION-SPEED-V2-WORKSPACE-no-game-data.zip`, SHA-256 `261ae036fadc1586c0af28827d346b24cf69fc0791b803776fcd13640b2e0fb8`
- Tested patch via reverse/application; source and workspace share identical source files.
- Compared with earlier Symbiose test VPK: all **17 ZIP members** retained, and only `eboot.bin` differs.
- Host C test passed under AddressSanitizer and UndefinedBehaviorSanitizer.
- The **new look speed is not yet hardware-verified**. The previously supplied log also contained no first-person possession log marker, so please check the new unique boot log after installing this build.

The VPK, source ZIP and workspace ZIP are downloadable as separate chat artifacts. They are intentionally **not** checked in to the public documentation repository, and no commercial Dungeon Keeper data is included.

## Vita hardware acceptance test

1. Back up game saves and install the test VPK via VitaShell.
2. Verify the **V2 start marker** in `ux0:data/keeperfx/keeperfx.log`.
3. Start level 4 and possess a creature. Confirm full-stick look is noticeably faster while small movements remain controllable.
4. Release the right stick: rotation must stop, without drift.
5. Check vertical look inversion, left-stick movement, return to dungeon, menu L/R, touch, audio and 960×544 display.
6. If anything remains wrong, send the latest log and state whether the turn rate is still too slow, too fast or inconsistent.
