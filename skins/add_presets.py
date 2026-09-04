"""Registers the race skins as Skin Shuffle presets.

    python skins/add_presets.py "<instance folder>"

e.g. python skins/add_presets.py "C:/Users/you/curseforge/minecraft/Instances/Medieval Fantasy Craft RPG"

Copies dwarf.png / elf.png / orc.png into the instance's Skin Shuffle skins
folder and adds a preset for each, leaving any existing presets alone.

Run with Minecraft CLOSED. Skin Shuffle keeps its presets in memory and rewrites
presets.json on exit, so edits made while the game is running are discarded.
"""

import io
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (preset name, skin file, base model). The elf is drawn on the slim (Alex)
# layout with 3px arms, so it must be registered as slim or its arms render wrong.
WANTED = [('Dwarf', 'dwarf', 'classic'),
          ('Elf', 'elf', 'slim'),
          ('Orc', 'orc', 'classic')]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2

    instance = sys.argv[1].replace('\\', '/').rstrip('/')
    base = os.path.join(instance, 'config', 'skinshuffle')
    skins = os.path.join(base, 'skins')
    presets_path = os.path.join(base, 'presets.json')

    if not os.path.isdir(base):
        print('Skin Shuffle config not found at %s' % base)
        print('Install Skin Shuffle and launch once, then re-run this.')
        return 1

    os.makedirs(skins, exist_ok=True)
    for _, key, _ in WANTED:
        src = os.path.join(HERE, key + '.png')
        if not os.path.isfile(src):
            print('missing source skin: %s' % src)
            return 1
        shutil.copy(src, os.path.join(skins, key + '.png'))
        print('copied %s.png' % key)

    if os.path.isfile(presets_path):
        data = json.load(io.open(presets_path, encoding='utf-8'))
    else:
        data = {'chosenPreset': 0, 'apiPreset': 0, 'loadedPresets': []}

    presets = data.setdefault('loadedPresets', [])
    existing = {p.get('name') for p in presets}

    added = 0
    for name, key, model in WANTED:
        if name in existing:
            print('%s: already a preset' % name)
            continue
        presets.append({
            'skin': {'skin_name': key, 'model': model, 'type': 'skinshuffle:config'},
            'name': name,
        })
        added += 1
        print('%s: preset added (%s model)' % (name, model))

    if added:
        io.open(presets_path, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(data, indent=2) + '\n')
        print('%d preset(s) written; carousel now holds %d' % (added, len(presets)))
    else:
        print('no changes needed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
