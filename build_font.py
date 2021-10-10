#!/usr/bin/env python

# I wrote most of this in the middle of the night.
# I know it's unreadable. I don't care.

import fontforge
from sys import argv;
import json
import cairosvg.surface
from PIL import Image, ImageChops
from io import BytesIO
font = fontforge.open(argv[1])
# sub -> name
outmap = {}
# name -> glyph
glyphs = {}

for glyph in font.glyphs():
    glyphs[glyph.glyphname] = glyph
    has_ligs = False
    for liga in glyph.getPosSub("*"):
        has_ligs = True
        iterator = iter(liga)
        next(iterator); next(iterator)
        new = map(lambda x: {
            "semicolon": ";",
            "space": " ",
            "colon": ":",
            "question": "?",
            "period": ".",
            "exclam": "!",
            "comma": ","
        }.get(x, x), iterator)
        final = "".join(new)
        if final[0].isupper() and not final.isupper():
            continue
        outmap[final] = glyph.glyphname
    if not has_ligs:
        if glyph.unicode == -1:
            continue
        outmap[chr(glyph.unicode)] = glyph.glyphname

# name -> point
name_map = {}
codepoint = 0xF000
for glyph in sorted(glyphs.keys()):
    name_map[glyph] = chr(codepoint) 
    codepoint += 1

# sub -> point
final_chars = {}
for (k, v) in outmap.items():
    final_chars[k] = name_map[v]

with open("subs.json", "w") as f:
    json.dump(final_chars, f)

# point -> (glyph, name)
glyph_map = {}
for (name, glyph) in glyphs.items():
    glyph_map[name_map[name]] = (glyph, name)

SIZE = 128

def svg2pil(*args, size=SIZE, dpi=96, **kwargs):
    t = cairosvg.surface.Tree(*args, **kwargs)
    f = BytesIO()
    cairosvg.surface.PNGSurface(t, f, dpi, parent_height=size, parent_width=size).finish()
    return Image.open(f)


output_img = Image.new("RGBA", (SIZE * 16, SIZE + len(glyph_map) // 16 * SIZE))
# chars = [["\u0000"] * 16] * (len(glyph_map) // 16 + 1)
chars = []
for i in range(len(glyph_map) // 16 + 1):
    row = []
    for i in range(16):
        row.append(chr(0))
    chars.append(row)
i = 0
for (point, (glyph, name)) in glyph_map.items():
    glyph.export("temp.svg")
    img = svg2pil(url='temp.svg')
    output_img.paste(img, (i % 16 * SIZE, i // 16 * SIZE))
    chars[i // 16][i % 16] = point
    i += 1
channels = output_img.split()
alpha = output_img.getchannel('A')
(red, green, blue, _) = map(lambda x: ImageChops.invert(x), channels)
output_img = Image.merge("RGBA", (red, green, blue, alpha))
output_img.save('out.png')

new_chars = []
for x in chars:
    new_chars.append("".join(x))

font_json = {
    "providers": [{
        "type": "bitmap",
        "file": "minecraft:font/sitelen_telo.png",
        "height": 12,
        "ascent": 9,
        "chars": new_chars
    }]
}

with open("font.json", "w") as f:
    json.dump(font_json, f)
