import yaml
import random
import re

with open("presentpast.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

subjects  = data['subjects']
activities = data['activities']
templates = data['templates']

def genrandomtask(data):
    # pick random template
    template = random.choice(data['templates'])
    # render task
    stream = next(iter(template))
    task = ""
    buf = ""
    choices = {}
    for char in stream:
        if char == "[":
            task += buf
            buf = ""
        elif char == ":":
            choice = random.choice(data[buf])
            choices[buf] = choice
            buf = ""
        elif char == "]":
            task += choice[buf]
            buf = ""
        else:
            buf += char
    task += buf

    # render solution
    stream = template[stream]
    solution = ""
    buf = ""
    for char in stream:
        if char == "[":
            solution += buf
            buf = ""
        elif char == ":":
            choice = choices[buf]
            buf = ""
        elif char == "]":
            solution += choice[buf]
            buf = ""
        else:
            buf += char
    solution += buf

    return task.capitalize(), solution.capitalize()

while True:
    task, solution = genrandomtask(data)
    print(task)
    input()
    print("Správná odpověď: {}\n".format(solution))
