# Example output:
# máma, venku, počítat, present simple
#
# cs_CZ: Máma venku počítá.
# en_US: Mom counts outside.
# de_DE: Mutti rechnet draußen.


import yaml
import random
import re

with open("dada.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

languages  = data['languages']
templates  = data['templates']
template   = 'present simple' 

def shuffle_random_sentence(template, langs):
    result = {}
    mode = "shuffle"
    choices = {}
    for lang in langs:
        buf = ""
        sentence = ""
        for char in template[lang]:
            if char == "[":
                sentence += buf
                buf = ""
            elif char == ":":
                if mode == "shuffle":
                    choice = random.choice(data[buf])
                    choices[buf] = choice
                elif mode == "translate":
                    choice = choices[buf]
                buf = ""
            elif char == "]":
                sentence += choice[buf]
                buf = ""
            else:
                buf += char
        sentence += buf
        result[lang] = "{}{}".format(sentence[0].upper(), sentence[1:])
        mode = "translate"

    return result, choices

snt, choices = shuffle_random_sentence(templates[template], languages)

words = []
for c in choices:
    words.append(choices[c][languages[0]])

print("{}, {}\n".format(", ".join(words), template))
for lang in snt:
    print("{}: {}".format(lang, snt[lang]))
