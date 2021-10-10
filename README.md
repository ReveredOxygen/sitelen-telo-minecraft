# sitelen telo resource pack

This is a resource pack that converts Minecraft's toki pona language
to the sitelen telo script. To use it, just add sitelen\_telo.zip to
your resource packs. **You do not need to unzip it**.  
I've tested it and found it to mostly work on
versions as low as 1.13, but it could work on lower.

Credit goes to u/efofecks for the sitelen
telo script, [found here][sitelen telo reddit].  
The toki pona translation is the translation found in
version 21w40a of Minecraft, for the PMC version of the resource pack.

## Known Issues

- The language name still appears in the Latin script. I can't figure out how to change it.
- Bold text looks weird

## Building

**You do not need to worry about this if you downloaded a .zip
of the resource pack**

It has only been tested with version 1.01 of sitelen telo.  
The build script has only been tested on Linux. It might work on macos,
but I don't know. I haven't tested it in WSL, but I don't see
why it wouldn't work.

The first step of building is to set it up. Make sure you have all the
packages in `requirements.txt`. You need to place the sitelen telo font
at the root of the repo as `font.otf`. You can download it from [here][sitelen telo gdrive]
You need to place the stock toki pona language file
(`tok.json` from the game files) at the root of the
reop as `lang.json`. You can download it from [here][tok.json] if you can't find it

Once you have the files, just run `./build.sh` and you should have the pack at `./lang.json`

[sitelen telo gdrive]: https://drive.google.com/file/d/1Y39JfjAfbthyECdTgcCZaKGR5i0Q7VUr/view?usp=sharing
[sitelen telo reddit]: https://www.reddit.com/r/tokipona/comments/jax1x2/sitelen_telo_v101_a_japaneseinspired_logographic/
[tok.json]: https://github.com/InventivetalentDev/minecraft-assets/blob/21w39a/assets/minecraft/lang/tok.json
