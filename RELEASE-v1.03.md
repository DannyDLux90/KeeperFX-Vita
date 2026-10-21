# KeeperFX Vita v1.03 — release and reproducibility notes

**Hardware-accepted program:** Controller RC4 (`KeeperFX-Vita-v1.03-CONTROLLER-RC4-TEST.vpk`).  
**Original hardware-tested RC4 VPK:** `KeeperFX-Vita-v1.03-FINAL-no-game-data.vpk`.
**Preferred final VPK (manual corrected):** `KeeperFX-Vita-v1.03-FINAL-MANUAL-UPDATE-no-game-data.vpk`.  
**Title ID:** `KFXV00001`.  
**Release SHA-256:** `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d`.

The public release has no commercial Dungeon Keeper game data. Copy assets from your own legally obtained copy to `ux0:data/keeperfx/`.

## Source and workspace delivery

Companion artifacts prepared with this release:

- `KeeperFX-Vita-v1.03-FINAL-SOURCE-no-game-data.zip` — complete retained source tree, Vita files, build scripts and open-source components already in the project snapshot; generated build products excluded.
- `KeeperFX-Vita-v1.03-FINAL-WORKSPACE-no-game-data.zip` — same tree plus built ARM/Vita artifacts, CMake/Ninja build metadata, matching ELF/debug symbols and VPK. Paths in cached metadata refer to the original environment.
- `KeeperFX-Vita-v1.03-FINAL-vs-original103.patch` — six-file unified diff against the 2026-09-20 v1.03 source snapshot.
- `CHANGELOG-v1.03.md` — v1.02 → v1.03 release notes.

**These large ZIP/VPK artifacts are provided separately, not stored as binaries in this documentation repository.** The project can link a release attachment or externally hosted archive here once published. Never substitute a private integrated game-data package.

## LiveArea manual documentation correction (2026-10-21)

The final packaging has been refreshed with the real v1.03 control layout in the LiveArea manual (six PNG pages). **The ARM/Vita executable is byte-for-byte identical** to the RC4 VPK, and the app retains `KFXV00001`. This is an asset-only revision; no game rebuild or additional gameplay changes.

Recommended download: `KeeperFX-Vita-v1.03-FINAL-MANUAL-UPDATE-no-game-data.vpk`  
SHA-256: `21f73fe8f8f223b3f40ce291da9544c956a66a858954b66fd2a9aeff78cb8a1d`

Accompanying updated source ZIP: `KeeperFX-Vita-v1.03-FINAL-MANUAL-UPDATE-SOURCE-no-game-data.zip`  
SHA-256: `1a05668965e33831d1b5ea8bec7d930769f125bc1dd2c0ecc5a5269ba8f85e3b`

Accompanying updated workspace ZIP: `KeeperFX-Vita-v1.03-FINAL-MANUAL-UPDATE-WORKSPACE-no-game-data.zip`  
SHA-256: `d425a71bd0f3019155f0c07bc268a3c94cb925fa30b748facf25a5163c8cdb33`

Full page description: [MANUAL-v1.03.md](MANUAL-v1.03.md).

## Artifact integrity

SHA-256:

| Artifact | SHA-256 |
|---|---|
| `KeeperFX-Vita-v1.03-FINAL-no-game-data.vpk` | `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d` |
| `KeeperFX-Vita-v1.03-FINAL-SOURCE-no-game-data.zip` | `9dbdd608f973381f26fc7e93131105191b28b1e5f65d516360b612d6c8e1747b` |
| `KeeperFX-Vita-v1.03-FINAL-WORKSPACE-no-game-data.zip` | `8298f13334cb23e6490c311cc8522d92466753318bf9d9dc283543d26b01edc0` |
| `patches/v1.03/v1.03-FINAL-vs-original103.patch` | `6756d04d9874fa6350efeb414af0c7c03143f1be26692a28d73bd27e5d3a45ef` |

The patch file is [committed to this repository](patches/v1.03/v1.03-FINAL-vs-original103.patch), while the full source and workspace ZIP files are distributed as separate downloadable companion artifacts.

## VitaSDK build requirements

The final workspace used VitaSDK at `/mnt/data/sdk_vita/vitasdk` in the original environment. On other machines, install matching VitaSDK toolchain and dependencies and reconfigure CMake; cached absolute paths must not be reused. Conceptual example:

```sh
export VITASDK=/path/to/vitasdk
cmake -S . -B out/build/vita-reldebug -G Ninja \
  -DCMAKE_TOOLCHAIN_FILE="$VITASDK/share/vita.toolchain.cmake" \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build out/build/vita-reldebug
```

Additional Vita build/dependency settings can be found in the source tree's `vita/` and CMake files and the archived CMake cache. The above is a build outline, **not a guarantee** that every dependency on a fresh machine is installed.

The release VPK was copied byte-for-byte from the hardware-tested RC4 binary; rebuilding on a different machine is not guaranteed byte-identical.

## Provenance and distribution

Unofficial Vita port based on upstream KeeperFX, pinned to commit `466e0753e17cee876f2ace6fa6b1e17f3ad44b0d`, under GPL-2.0 with third-party dependencies subject to their original licences. **No commercial Dungeon Keeper assets**, private VPKs, user game saves, crash dumps, recording data or VitaSDK binaries are part of the public source/workspace archives. Experimental alternate video and recording builds were not included in v1.03 final.
