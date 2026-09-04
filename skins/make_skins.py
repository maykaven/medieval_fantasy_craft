"""High-detail 64x64 race skins: dwarf, elf, orc.

Rectangle fills cannot express a face. Every visible surface here is a
hand-authored pixel map - one character per pixel against a per-race palette -
so features like a mouth inside a beard, cheekbones, tendons and beard rings are
placed deliberately rather than approximated with bands.

Two structural ideas carry over:
  * Features cross body parts: the dwarf's beard is painted on the torso too, so
    it runs unbroken from his chin to his belt.
  * Layer 2 is geometry: 3D Skin Layers gives the outer layer real depth, so
    beards, hair and harnesses stand off the model.

Stdlib only - no PIL.
"""

import os
import struct
import sys
import zlib

W = H = 64
CLEAR = (0, 0, 0, 0)


def sh(c, f):
    r, g, b, a = c
    return (max(0, min(255, int(r * f))), max(0, min(255, int(g * f))),
            max(0, min(255, int(b * f))), a)


def blank():
    return [[CLEAR for _ in range(W)] for _ in range(H)]


def write_png(path, px):
    raw = bytearray()
    for row in px:
        raw.append(0)
        for r, g, b, a in row:
            raw += bytes((r, g, b, a))

    def chunk(tag, data):
        return (struct.pack('>I', len(data)) + tag + data
                + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff))

    blob = (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', W, H, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(bytes(raw), 9))
            + chunk(b'IEND', b''))
    open(path, 'wb').write(blob)
    return len(blob)


def faces(ox, oy, w, d, h):
    return {'top': (ox + d, oy, w, d), 'bottom': (ox + d + w, oy, w, d),
            'right': (ox, oy + d, d, h), 'front': (ox + d, oy + d, w, h),
            'left': (ox + d + w, oy + d, d, h), 'back': (ox + d + w + d, oy + d, w, h)}


HEAD, HAT = faces(0, 0, 8, 8, 8), faces(32, 0, 8, 8, 8)
BODY, JACKET = faces(16, 16, 8, 4, 12), faces(16, 32, 8, 4, 12)
ARM_R, SLEEVE_R = faces(40, 16, 4, 4, 12), faces(40, 32, 4, 4, 12)
ARM_L, SLEEVE_L = faces(32, 48, 4, 4, 12), faces(48, 48, 4, 4, 12)
ARM_R3, SLEEVE_R3 = faces(40, 16, 3, 4, 12), faces(40, 32, 3, 4, 12)
ARM_L3, SLEEVE_L3 = faces(32, 48, 3, 4, 12), faces(48, 48, 3, 4, 12)
LEG_R, TROUSER_R = faces(0, 16, 4, 4, 12), faces(0, 32, 4, 4, 12)
LEG_L, TROUSER_L = faces(16, 48, 4, 4, 12), faces(0, 48, 4, 4, 12)

SIDE = {'front': 1.0, 'right': 0.87, 'left': 0.95, 'back': 0.79, 'top': 1.13, 'bottom': 0.68}


def draw(px, box, rows, pal, light=1.0):
    """Paint a pixel map into a UV box. '.' leaves the pixel untouched."""
    x0, y0, bw, bh = box
    for j, row in enumerate(rows):
        if j >= bh:
            break
        for i, ch in enumerate(row):
            if i >= bw or ch == '.':
                continue
            c = pal[ch]
            px[y0 + j][x0 + i] = c if light == 1.0 else sh(c, light)


def fill(px, box, c):
    x0, y0, bw, bh = box
    for y in range(y0, y0 + bh):
        for x in range(x0, x0 + bw):
            px[y][x] = c


def flip(rows):
    return [r[::-1] for r in rows]


def solid(px, part, rows_by_face, pal, base):
    """Draw authored faces; fill anything unauthored with a lit base tone."""
    for face, box in part.items():
        rows = rows_by_face.get(face)
        if rows is None:
            fill(px, box, sh(base, SIDE[face]))
        else:
            fill(px, box, sh(base, SIDE[face]))
            draw(px, box, rows, pal, SIDE[face])


# ===========================================================================
# DWARF - beard to the belt, and a mouth inside it
# ===========================================================================
def dwarf(px):
    P = {
        'S': (206, 146, 84, 255), 'l': (226, 170, 110, 255),
        's': (172, 116, 62, 255), 'D': (132, 84, 44, 255),
        'H': (108, 42, 18, 255), 'h': (152, 64, 26, 255), 'L': (186, 92, 44, 255),
        'W': (246, 242, 230, 255), 'I': (78, 48, 26, 255),
        'M': (72, 34, 22, 255), 'm': (176, 96, 84, 255),
        'T': (104, 62, 38, 255), 't': (128, 80, 50, 255), 'K': (74, 44, 26, 255),
        'B': (58, 38, 24, 255), 'G': (206, 166, 72, 255), 'g': (150, 116, 44, 255),
        'E': (158, 162, 170, 255), 'e': (104, 108, 116, 255),
    }
    head_front = [
        "HHHHHHHH",
        "HhLhhLhH",
        "sSSSSSSs",
        "SWIsSIWS",
        "SslLLsSS",
        "hhhhhhhh",
        "hHmMMmHh",
        "hLhHHhLh",
    ]
    head_right = [
        "HHHHHHHH",
        "HhhLhhhH",
        "sSSSSSSs",
        "SSSSSsWS",
        "SSSSSSlS",
        "hhhhhhhh",
        "hhHhhHhh",
        "hLhhhhLh",
    ]
    head_back = [
        "HHHHHHHH",
        "HLhhhhLH",
        "HhhHHhhH",
        "HhLhhLhH",
        "hhhHHhhh",
        "hLhhhhLh",
        "hhHhhHhh",
        "HhhhhhhH",
    ]
    solid(px, HEAD, {'front': head_front, 'right': head_right,
                     'left': flip(head_right), 'back': head_back,
                     'top': head_back}, P, P['S'])
    fill(px, HEAD['bottom'], P['D'])

    # layer 2: the beard as geometry, braid rings either side
    hat_front = [
        "........",
        "........",
        "........",
        "........",
        ".hhhhhh.",
        "hHhhhhHh",
        "hG....Gh",
        ".hHhhHh.",
    ]
    # layer 2 must stay transparent where unauthored, so never fill it first
    for f in HAT:
        fill(px, HAT[f], CLEAR)
    draw(px, HAT['front'], hat_front, P)
    draw(px, HAT['right'], ["........", "........", "........", "........",
                            "....hhhh", "...hHhhh", "...hhhhh", "....hHhh"], P, SIDE['right'])
    draw(px, HAT['left'], ["........", "........", "........", "........",
                           "hhhh....", "hhhHh...", "hhhhh...", "hhHh...."], P, SIDE['left'])
    draw(px, HAT['back'], ["........", ".LhhhhL.", ".hhHHhh.", ".hLhhLh.",
                           ".hhhHhh.", ".hHhhHh.", "..hhhh..", "........"], P, SIDE['back'])

    # torso: beard down the chest, tunic either side, belt at the hem
    body_front = [
        "TthhhhtT",
        "TthhhhtT",
        "ThHhhHhT",
        "ThGhhGhT",
        "TthhhhtT",
        "TthHHhtT",
        "TthhhhtT",
        "TthHHhtT",
        "TtthhttT",
        "BBBBBBBB",
        "BBBGGBBB",
        "KKKgKKKK",
    ]
    body_back = [
        "TtttttttT"[:8],
        "TttttttT",
        "TtKKKKtT",
        "TtttttttT"[:8],
        "TttttttT",
        "TtKKKKtT",
        "TttttttT",
        "TttttttT",
        "TttttttT",
        "BBBBBBBB",
        "BBBBBBBB",
        "KKKKKKKK",
    ]
    solid(px, BODY, {'front': body_front, 'back': body_back}, P, P['T'])
    jacket_front = [
        ".hhhhhh.",
        ".hHhhHh.",
        ".hhhhhh.",
        ".hGhhGh.",
        ".hhhhhh.",
        ".hHhhHh.",
        ".hhhhhh.",
        "..hHHh..",
        "..hhhh..",
        "........",
        "........",
        "........",
    ]
    for f in JACKET:
        fill(px, JACKET[f], CLEAR)
    draw(px, JACKET['front'], jacket_front, P)

    arm_front = ["TttT", "TttT", "TttT", "TttT", "TttT", "TttT", "TttT",
                 "BBBB", "BBBB", "SllS", "SssS", "sDDs"]
    for arm, sleeve in ((ARM_R, SLEEVE_R), (ARM_L, SLEEVE_L)):
        solid(px, arm, {'front': arm_front, 'back': arm_front,
                        'right': arm_front, 'left': arm_front}, P, P['T'])
        fill(px, arm['bottom'], P['s'])
        for f in sleeve:
            fill(px, sleeve[f], CLEAR)
        draw(px, sleeve['front'], ["....", "....", "....", "....", "....", "....",
                                   "EEEE", "eEEe", "EeeE", "....", "....", "...."], P)

    leg_front = ["KKKK", "KttK", "KttK", "KttK", "KttK", "KttK", "KttK",
                 "EBBE", "BBBB", "BKKB", "BBBB", "KKKK"]
    for leg in (LEG_R, LEG_L):
        solid(px, leg, {'front': leg_front, 'back': leg_front,
                        'right': leg_front, 'left': leg_front}, P, P['K'])
        fill(px, leg['bottom'], sh(P['B'], 0.7))
    for t in (TROUSER_R, TROUSER_L):
        for f in t:
            fill(px, t[f], CLEAR)


# ===========================================================================
# ELF - slim build, tailored clothes, circlet
# ===========================================================================
def elf(px):
    P = {
        'S': (245, 220, 200, 255), 'l': (255, 236, 220, 255),
        's': (214, 184, 164, 255), 'D': (176, 146, 128, 255),
        'H': (198, 178, 118, 255), 'h': (228, 210, 152, 255), 'L': (246, 234, 190, 255),
        'W': (250, 248, 242, 255), 'I': (48, 112, 92, 255),
        'm': (206, 146, 138, 255), 'M': (150, 100, 96, 255),
        'C': (44, 106, 74, 255), 'c': (58, 124, 90, 255), 'd': (30, 78, 56, 255),
        'G': (212, 182, 100, 255), 'g': (156, 128, 62, 255),
        'K': (28, 62, 52, 255), 'B': (86, 66, 44, 255), 'b': (62, 46, 30, 255),
    }
    head_front = [
        "hhhhhhhh",
        "hGGGGGGh",
        "hsSSSSsh",
        "hWIsSIWh",
        "hSslLsSh",
        "hSSllSSh",
        "hSMmmMSh",
        "hsSSSSsh",
    ]
    head_right = [
        "hhhhhhhh",
        "hhhGGhhh",
        "hhhhhSSh",
        "hhhhhSlS",
        "hhhhhSsS",
        "hhhhhSSh",
        "hhhhhhSh",
        "hhhhhhhh",
    ]
    head_back = [
        "hhhhhhhh",
        "hGGGGGGh",
        "hLhhhhLh",
        "hhHHHHhh",
        "hLhhhhLh",
        "hhHHHHhh",
        "hLhhhhLh",
        "hhhhhhhh",
    ]
    solid(px, HEAD, {'front': head_front, 'right': head_right,
                     'left': flip(head_right), 'back': head_back,
                     'top': head_back}, P, P['S'])
    fill(px, HEAD['bottom'], P['D'])
    # bare pointed ear tips against the hair
    px[HEAD['right'][1] + 3][HEAD['right'][0] + 6] = P['S']
    px[HEAD['right'][1] + 4][HEAD['right'][0] + 6] = P['s']
    px[HEAD['left'][1] + 3][HEAD['left'][0] + 1] = P['S']
    px[HEAD['left'][1] + 4][HEAD['left'][0] + 1] = P['s']

    # layer 2: hair mane with strand detail
    for f in HAT:
        fill(px, HAT[f], CLEAR)
    draw(px, HAT['front'], ["hhhhhhhh", "hLhhhhLh", "h......h", "h......h",
                            "h......h", "h......h", "h......h", ".h....h."], P)
    draw(px, HAT['right'], ["hhhhhhhh", "hhhLhhhh", "hhHhhhh.", "hhhhhhh.",
                            "hhHhhhh.", "hhhhhhh.", "hhHhhh..", "hhhh...."], P, SIDE['right'])
    draw(px, HAT['left'], flip(["hhhhhhhh", "hhhLhhhh", "hhHhhhh.", "hhhhhhh.",
                                "hhHhhhh.", "hhhhhhh.", "hhHhhh..", "hhhh...."]), P, SIDE['left'])
    draw(px, HAT['back'], ["hhhhhhhh", "hLhhhhLh", "hhHHHHhh", "hLhhhhLh",
                           "hhHHHHhh", "hLhhhhLh", ".hhHHhh.", "..hhhh.."], P, SIDE['back'])
    draw(px, HAT['top'], ["hhhhhhhh", "hLLLLLLh", "hLhhhhLh", "hhhhhhhh",
                          "hhhhhhhh", "hLhhhhLh", "hLLLLLLh", "hhhhhhhh"], P, SIDE['top'])

    body_front = [
        "CcGGGGcC",
        "CcGddGcC",
        "CGcdd cG"[:8].replace(' ', 'c'),
        "CcGddGcC",
        "GcCddCcG",
        "CcGddGcC",
        "CGcddcGC",
        "bbbGGbbb",
        "CcCddCcC",
        "CcGddGcC",
        "CdcddcdC",
        "GGGGGGGG",
    ]
    body_back = [
        "KKKKKKKK",
        "KGGGGGGK",
        "KKddddKK",
        "KdKKKKdK",
        "KKddddKK",
        "KdKKKKdK",
        "KKddddKK",
        "KdKKKKdK",
        "KKddddKK",
        "KdKKKKdK",
        "KKddddKK",
        "KGGGGGGK",
    ]
    solid(px, BODY, {'front': body_front, 'back': body_back}, P, P['C'])
    # layer 2: cloak off the shoulders and down the back
    for f in JACKET:
        fill(px, JACKET[f], CLEAR)
    draw(px, JACKET['back'], ["KGGGGGGK", "KKddddKK", "KdKKKKdK", "KKddddKK",
                              "KdKKKKdK", "KKddddKK", "KdKKKKdK", "KKddddKK",
                              "KdKKKKdK", "KKddddKK", ".KddddK.", "..KKKK.."], P, SIDE['back'])
    draw(px, JACKET['right'], ["KKKK", "KddK", "KdKK", "KKdd", "KddK", "KdKK",
                               "KKdd", "KddK", "KdKK", "KKdd", ".KdK", ".KK."], P, SIDE['right'])
    draw(px, JACKET['left'], ["KKKK", "KddK", "KKdK", "ddKK", "KddK", "KKdK",
                              "ddKK", "KddK", "KKdK", "ddKK", "KdK.", ".KK."], P, SIDE['left'])
    draw(px, JACKET['front'], ["..GG..", "..GG.."], P)

    arm_front = ["Ccc", "Ccc", "CcG", "Ccc", "Ccc", "CcG", "Ccc",
                 "GGG", "SlS", "SSs", "sSs", "sDD"]
    for arm, sleeve in ((ARM_R3, SLEEVE_R3), (ARM_L3, SLEEVE_L3)):
        solid(px, arm, {'front': arm_front, 'back': arm_front,
                        'right': arm_front, 'left': arm_front}, P, P['C'])
        fill(px, arm['bottom'], P['s'])
        for f in sleeve:
            fill(px, sleeve[f], CLEAR)

    leg_front = ["dCCd", "dccd", "dCcd", "dccd", "dCcd", "GGGG",
                 "BbbB", "BBbB", "BbbB", "GGGG", "bBBb", "bbbb"]
    for leg in (LEG_R, LEG_L):
        solid(px, leg, {'front': leg_front, 'back': leg_front,
                        'right': leg_front, 'left': leg_front}, P, (62, 88, 66, 255))
        fill(px, leg['bottom'], sh(P['b'], 0.8))
    for t in (TROUSER_R, TROUSER_L):
        for f in t:
            fill(px, t[f], CLEAR)


# ===========================================================================
# ORC - the one that worked; pushed further
# ===========================================================================
def orc(px):
    P = {
        'S': (120, 152, 68, 255), 'l': (146, 178, 88, 255), 'L': (166, 196, 108, 255),
        's': (94, 122, 52, 255), 'D': (68, 92, 38, 255), 'X': (48, 66, 26, 255),
        'H': (34, 32, 30, 255), 'h': (54, 50, 46, 255),
        'W': (238, 228, 200, 255), 'I': (168, 46, 34, 255),
        'T': (240, 236, 218, 255), 't': (196, 190, 170, 255),
        'K': (92, 62, 40, 255), 'k': (118, 82, 54, 255), 'B': (58, 39, 25, 255),
        'E': (132, 134, 140, 255), 'e': (92, 94, 100, 255),
        'P': (176, 66, 54, 255),
    }
    head_front = [
        "HHHHHHHH",
        "HhhhhhhH",
        "XXsssXXX"[:8],
        "sWIsSIWs",
        "SsllLlsS",
        "STsllsTS",
        "SsXXXXsS",
        "sSTssTSs",
    ]
    head_right = [
        "HHHHHHHH",
        "HhhhhhhH",
        "SSSXXXXs",
        "SSSSSsWs",
        "SlLllllS",
        "SSllllTS",
        "SsSSssXs",
        "sSSSSsTs",
    ]
    head_back = [
        "HHHHHHHH",
        "HhHhhHhH",
        "HhhhhhhH",
        "sSSSSSSs",
        "SsLllLsS",
        "SSsllsSS",
        "sSSSSSSs",
        "sssssssss"[:8],
    ]
    solid(px, HEAD, {'front': head_front, 'right': head_right,
                     'left': flip(head_right), 'back': head_back,
                     'top': head_back}, P, P['S'])
    fill(px, HEAD['bottom'], P['X'])
    # warpaint stripes across the eyes
    for x in (1, 3, 6):
        px[HEAD['front'][1] + 2][HEAD['front'][0] + x] = P['P']

    # layer 2: topknot and braid
    for f in HAT:
        fill(px, HAT[f], CLEAR)
    draw(px, HAT['top'], ["........", "..HHHH..", ".HhhhhH.", ".HhHHhH.",
                          ".HhhhhH.", "..HHHH..", "........", "........"], P, SIDE['top'])
    draw(px, HAT['back'], ["...HH...", "...hh...", "...Hh...", "...hh...",
                           "...Hh...", "...hh...", "...EE...", "........"], P, SIDE['back'])
    draw(px, HAT['front'], ["HHHHHHHH", "HhhhhhhH", "........", "........",
                            "........", "........", "........", "........"], P)

    body_front = [
        "sLllllLs",
        "SLlssllL"[:8],
        "SlLsslLS",
        "SlLsslLS",
        "SsLssLsS",
        "sSDssDSs",
        "SsXsXsXS"[:8],
        "SsDDDDsS",
        "SsXDDXsS",
        "SsDDDDsS",
        "sSXDDXSs",
        "XssssssX",
    ]
    body_back = [
        "sLllllLs",
        "SlDssDlS",
        "SlXssXlS",
        "SsDssDsS",
        "SsXssXsS",
        "SsDssDsS",
        "SssssssS",
        "SsDDDDsS",
        "SssssssS",
        "SsXXXXsS",
        "SssssssS",
        "XssssssX",
    ]
    solid(px, BODY, {'front': body_front, 'back': body_back}, P, P['S'])
    # layer 2: diagonal harness, riveted belt
    for f in JACKET:
        fill(px, JACKET[f], CLEAR)
    draw(px, JACKET['front'], ["Kk......", ".Kk.....", "..Kk....", "...Kk...",
                               "....Kk..", ".....Kk.", "......Kk", "........",
                               "KKKKKKKK", "KkEEkKKK", "BBBBBBBB", "........"], P)
    draw(px, JACKET['back'], ["........", "........", "........", "........",
                              "........", "........", "........", "........",
                              "BBBBBBBB", "BkkkkkkB", "BBBBBBBB", "........"], P, SIDE['back'])

    arm_front = ["sLLs", "LllL", "LllL", "SllS", "SsDS"[:4], "SllS", "SllS",
                 "sSSs", "KkkK", "KKKK", "SllS", "sDDs"]
    for arm, sleeve in ((ARM_R, SLEEVE_R), (ARM_L, SLEEVE_L)):
        solid(px, arm, {'front': arm_front, 'back': arm_front,
                        'right': arm_front, 'left': arm_front}, P, P['S'])
        fill(px, arm['bottom'], P['s'])
        for f in sleeve:
            fill(px, sleeve[f], CLEAR)
        draw(px, sleeve['front'], ["BKKB", "BkkB", "EBBE", "....", "....", "....",
                                   "....", "....", "....", "....", "....", "...."], P)

    leg_front = ["KkkK", "KkkK", "KKkK", "KkkK", "BKKB", "SllS",
                 "SssS", "SllS", "BbbB"[:4].replace('b', 'B'), "BBBB", "BKKB", "BBBB"]
    for leg in (LEG_R, LEG_L):
        solid(px, leg, {'front': leg_front, 'back': leg_front,
                        'right': leg_front, 'left': leg_front}, P, P['S'])
        fill(px, leg['bottom'], sh(P['B'], 0.7))
    for t in (TROUSER_R, TROUSER_L):
        for f in t:
            fill(px, t[f], CLEAR)
        draw(px, t['front'], ["KkkK", "KkkK", "KKkK", "KkkK", "BKKB", "........"[:4],
                              "....", "....", "....", "....", "....", "...."], P)


RACES = {'dwarf': dwarf, 'elf': elf, 'orc': orc}


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out, exist_ok=True)
    for name, painter in RACES.items():
        px = blank()
        painter(px)
        size = write_png(os.path.join(out, name + '.png'), px)
        print('  %-6s -> %s.png (%d bytes)' % (name, name, size))
    return 0


if __name__ == '__main__':
    sys.exit(main())
