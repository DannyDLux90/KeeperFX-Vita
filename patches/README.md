# Patch/source state

This directory contains the pieces that describe the currently tested Vita line.

## `post-v14/patch_v14_local_packet_history.py`

Restores a 40-turn local packet-history ring when KeeperFX networking is disabled. KeeperFX still relies on packet history for local camera/input processing, so the original no-op stub caused broken local movement/control behavior.

## `post-v14/patch_network_probe.py`

Experimental, unfinished Vita LAN/direct-IP networking probe. **Not part of the stable v1.02 public build.** See `NETWORK.md`.

## `v1.02/helpers.s`

Exact helper assembly used by the hardware-tested German v1.02 post-link patch. It contains:

- Vita system-language mapping into KeeperFX language IDs;
- the then-current local quit helper.

Important: the language path is hardware-confirmed. The quit helper is **not** a completed fix; in-game Quit remains a known issue.

## Why post-link patches exist

During hardware debugging, several Vita-specific defects were isolated at the binary/VELF level before the corresponding clean source-only integration was completed. The current public binary therefore combines the Vita source baseline with a small number of verified post-link modifications.

The project goal is to move every validated change back into normal source code and produce an exact clean source-only v1.02+ rebuild.

## Stable invariants that must not regress

- local 40-turn packet history;
- valid transferred-creature model guard (accept current tested models 1..36, reject model 0/corruption);
- rear touch disabled;
- Cross = left click / Circle = right click;
- Vita system language applied before language-dependent resource selection;
- logger path must not call the unavailable/broken Vita `sceClibPrintf` route that previously caused an early crash;
- known-good LiveArea/bubble assets must be retained.
