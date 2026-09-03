"""Prints the compile classpath for racescale, one entry per ';'.

Minecraft's own dependencies (fastutil, jspecify, sponge-mixin, fabric-loader,
blaze3d's transitive deps...) live in the launcher's libraries folder, so the
whole readable set goes on the classpath rather than being chased one missing
class at a time.

Two things are filtered out:
  * Forge / NeoForge jars - irrelevant to a Fabric mod, and the launcher keeps a
    truncated forge jar that javac refuses to read ("zip END header not found").
  * anything that will not open as a zip, for the same reason.
"""

import os
import sys
import zipfile


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: classpath.py <mc_install> <mc_jar>", file=sys.stderr)
        return 2

    install, mc_jar = sys.argv[1], sys.argv[2]
    entries = [mc_jar.replace("\\", "/")]
    skipped = 0

    lib_root = os.path.join(install, "libraries")
    found = []
    for dirpath, _dirnames, filenames in os.walk(lib_root):
        for name in filenames:
            if name.endswith(".jar"):
                found.append(os.path.join(dirpath, name))

    for path in sorted(found):
        normalised = path.replace("\\", "/")
        # Match against the path *below* libraries: the install directory itself
        # is "curseforge", which contains "forge" and would exclude everything.
        relative = os.path.relpath(path, lib_root).replace("\\", "/").lower()
        if "forge" in relative:
            continue
        try:
            with zipfile.ZipFile(path):
                pass
        except Exception:
            skipped += 1
            continue
        entries.append(normalised)

    if skipped:
        print("skipped %d unreadable jar(s)" % skipped, file=sys.stderr)

    print(";".join(entries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
