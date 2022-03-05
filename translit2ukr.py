#!/usr/bin/env python3

# Program to transliterate Czech text (stdin) to Ukrainian cyrillic (stdout)
# using German standard DIN 1460 plus some Czech specifics
# Dependency: iblingua-translit-perl (translit program that supports DIN 1460)
#
# Author: Vaclav Sistek <vsistek@fsfe.org>

import re
import sys
import subprocess

text = sys.stdin.read()
text = subprocess.run(['translit', '-t', "DIN 1460 UKR", '-r'],
       stdout=subprocess.PIPE, input=text, encoding='utf8').stdout
subs = [['ř', 'рж'],
        ['Ř', 'Рж'],
        ['ď', 'дь'],
        ['Ď', 'Дь'],
        ['ť', 'ть'],
        ['Ť', 'Ть'],
        ['ň', 'нь'],
        ['Ň', 'Нь'],
        ['á', 'а'],
        ['Á', 'А'],
        ['é', 'е'],
        ['É', 'Е'],
        ['ě', 'є'],
        ['Ě', 'Є'],
        ['í', 'і'],
        ['Í', 'I'],
        ['ý', 'и'],
        ['Ý', 'И'],
        ['ó', 'о'],
        ['Ó', 'О'],
        ['ů', 'у'],
        ['Ů', 'У'],
        ['йі', 'ї'],
        ['Йі', 'Ї']]
for s in subs:
    text = re.sub(s[0], s[1], text)

print(text)
