#!/usr/bin/env bash
# Builds racescale without Fabric Loom.
#
# Loom exists to remap Minecraft between obfuscated / intermediary / named names.
# Minecraft 26.x ships DEOBFUSCATED: Mojang publishes no client_mappings in the
# version manifest, and Fabric intermediary is the identity map (version 0.0.0).
# Loom 1.17.20 has no working configuration for that - officialMojangMappings()
# cannot find a map, and an empty layered spec throws a NullPointerException - so
# we compile straight against the game jar instead. Runtime names equal
# compile-time names, which is also why the mixin config needs no refmap.
#
# Requires JDK 25: Minecraft 26.2's classes are major version 69, which older
# javac cannot read.
set -e

JAVA_HOME="${JAVA_HOME:-/c/Program Files/Microsoft/jdk-25.0.4.101-hotspot}"
MC_INSTALL="${MC_INSTALL:-C:/Users/mayka/curseforge/minecraft/Install}"
MC_VERSION="${MC_VERSION:-26.2}"
MOD_VERSION=0.1.0

MC_JAR="$MC_INSTALL/versions/$MC_VERSION/$MC_VERSION.jar"
[ -f "$MC_JAR" ] || { echo "Minecraft jar not found: $MC_JAR" >&2; exit 1; }

CP="$(python classpath.py "$MC_INSTALL" "$MC_JAR")"

rm -rf build/classes
mkdir -p build/classes build/libs

"$JAVA_HOME/bin/javac.exe" --release 25 -encoding UTF-8 -nowarn -cp "$CP" \
    -d build/classes $(find src/main/java -name '*.java')

"$JAVA_HOME/bin/jar.exe" --create --file "build/libs/racescale-$MOD_VERSION.jar" \
    -C build/classes . -C src/main/resources .

echo "Built build/libs/racescale-$MOD_VERSION.jar"
