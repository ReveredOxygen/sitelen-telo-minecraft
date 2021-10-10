#!/usr/bin/env python

import json

subs_dict = None
with open("subs.json", "r") as f:
    subs_dict = json.load(f)

# subs_dict['Manka'] = "".join(list(map(lambda x: subs_dict[x], ['[', 'MA', 'N', 'KA', ']'])))


lang = None
with open("lang.json", "r") as f:
    lang = json.load(f)

subs = list(subs_dict.items())
subs.sort(key=lambda x: len(x[0]), reverse=True)

subs = list(filter(lambda x: x[0] not in ["s", "%"], subs))

def patch(string):
    uppercasing = False
    new = []
    for x in list(string):
        if x.isupper() and not uppercasing:
            new += '[' + x
            uppercasing = True
        elif uppercasing:
            if not x.isalpha():
                new += ']' + x
                uppercasing = False
            else:
                new += x.upper()
        else:
            new += x
    if uppercasing:
        new += ']'
    string = "".join(new)

    for sub in subs:
        string = string.replace(sub[0], sub[1])
    return string

i = 0
for (k, v) in lang.items():
    i += 1
    lang[k] = patch(lang[k])

with open("new_lang.json", "w") as f:
    json.dump(lang, f)

with open("pack.mcmeta", "w") as f:
    json.dump({
        "pack": {
            "description": "o tan ni: toki pona li kepeken e sitelen telo",
            "pack_format": 7
            },
        "language": {
            "tok": {
                "name": patch("tokipona"),
                "region": patch("ma pona"),
                "bidirectional": False
            }
            }
        }, f)
