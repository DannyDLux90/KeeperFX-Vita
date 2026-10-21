# Sources / upstream references

KeeperFX Vita is a community/homebrew porting effort. The public release does **not** include commercial Dungeon Keeper game data.

## KeeperFX upstream

Primary upstream project:

- https://github.com/dkfans/keeperfx

Pinned KeeperFX base commit used for this development line:

- https://github.com/dkfans/keeperfx/commit/466e0753e17cee876f2ace6fa6b1e17f3ad44b0d
- SHA: `466e0753e17cee876f2ace6fa6b1e17f3ad44b0d`

That commit is the merge of the PC OpenGL renderer work used as the upstream base for the Vita development snapshot.

A historical development fork used during the Vita port work is also available at:

- https://github.com/cerwym/keeperfx

Some old helper/build branches referenced by local handoff notes no longer exist on the public fork; therefore this repository documents the local source/patch state instead of relying on those branches remaining available forever.

## Vita toolchain / SDK

The Vita build uses the public vitaSDK ecosystem, including the Vita ELF/SELF/VPK toolchain:

- vitaSDK organization: https://github.com/vitasdk
- vita-toolchain: https://github.com/vitasdk/vita-toolchain

Development artifacts for this line used a vitaSDK 2026.08-era environment. Locally retained packages include `vitasdk-core-2026.08.1`, zlib, libpng, libjpeg-turbo, FreeType and Vita libraries required by the port.

The final Vita executable packaging flow uses the normal Vita tools (including `vita-elf-create` before `vita-make-fself`). Skipping the Vita ELF conversion step was previously proven to produce an invalid Vita ELF/SELF and is not part of the stable build process.

## vitaGL

The Vita renderer uses vitaGL / GXM presentation work:

- https://github.com/Rinnegatamante/vitaGL

The current Vita renderer path keeps KeeperFX's PAL8/software game rendering logic and uses vitaGL for the Vita presentation/palette-shader path.

## VitaShell

VitaShell is the recommended VPK/file-management utility for installation and log/data transfer:

- https://github.com/TheOfficialFloW/VitaShell

## SDL2 / other open-source dependencies

KeeperFX itself uses SDL2 and other open-source libraries. Refer to the upstream KeeperFX source tree and its build files for the complete dependency and license set.

The Vita-specific source snapshot also includes references/build integration for libraries such as FreeType, zlib, libpng, libjpeg-turbo, minizip and (for experimental networking only) ENet6.

## Commercial Dungeon Keeper data

Dungeon Keeper game assets are **not open-source dependencies of this repository** and are not included in the public VPK/source package.

Users must provide game files from their own legally obtained copy (for example CD or GOG) as described in `INSTALL.md`.

## Licensing

KeeperFX source is distributed under GNU GPL v2. The modifications in this repository follow that license. Individual third-party dependencies remain under their respective upstream licenses.


## Final Vita v1.03 source and workspace

The **final 1.03 source archive** contains the retained 2026-09-20 Vita source tree plus six updated source files implementing native KVF intro preroll, minimap bounds/capacity correction and final RC4 controller navigation. A corresponding **workspace archive** includes the compiled ARM binary, debug symbols, Vita SELF/VPK and original CMake/Ninja build metadata. These archives were prepared separately from this documentation repository and are not stored here as binary Git blobs. See [RELEASE-v1.03.md](RELEASE-v1.03.md) and [CHANGELOG-v1.03.md](CHANGELOG-v1.03.md).

The confirmed final no-game-data VPK SHA-256 is `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d`. Reproducing a source build needs the compatible VitaSDK and third-party toolchain components; the archives do **not** include the SDK or commercial game data.
