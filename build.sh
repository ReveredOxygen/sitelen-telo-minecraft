#!/bin/sh 

mkdir -p sitelen\ telo/assets/minecraft
mkdir sitelen\ telo/assets/minecraft/font
mkdir sitelen\ telo/assets/minecraft/lang
mkdir -p sitelen\ telo/assets/minecraft/textures/font

./build_font.py font.otf
./patch_lang.py

cp new_lang.json "sitelen telo/assets/minecraft/lang/tok.json"
cp out.png "sitelen telo/assets/minecraft/textures/font/sitelen_telo.png"
cp font.json "sitelen telo/assets/minecraft/font/default.json"
cp pack.mcmeta "sitelen telo"
cp README.md "sitelen telo"

cd "sitelen telo"
zip -r ../sitelen_telo.zip *
cd ..
