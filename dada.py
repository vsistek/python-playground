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
        result[lang] = sentence.capitalize()
        mode = "translate"

    return result

snt = shuffle_random_sentence(templates['present_simple'], languages)
for lang in snt:
    print("{}: {}".format(lang, snt[lang]))
