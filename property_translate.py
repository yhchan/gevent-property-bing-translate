#!/usr/bin/env python

# coding: utf-8

import config
from parse.properties import parse_properties
from translate.microsoft import Translator


def main():
    langs = parse_properties(config.FILE_FROM)
    translator = Translator(config.BING_APPID,
                            config.LANG_FROM,
                            config.LANG_TO)

    texts = [text if text else "" for text in langs.values()]
    trans = translator.translate_list(texts)
    translated = dict(zip(langs.keys(), trans))

    with open(config.FILE_TO, 'w+') as f:
        for k, v in sorted(translated.items()):
            f.write("%s=%s\n" % (k, v))

if __name__ == '__main__':
    main()
