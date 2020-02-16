import yaml
import random
import re

with open("presentpast.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def genrandomtask(data):
    # pick random template
    template = random.choice(data['templates'])
    choices = {}
    mode = "task"
    for stream in template: 
        out = ""
        buf = ""
        for char in stream:
            if char == "[":
                out += buf
                buf = ""
            elif char == ":":
                if mode == "task":
                    choice = random.choice(data[buf])
                    choices[buf] = choice
                    buf = ""
                elif mode == "solution":
                    choice = choices[buf]
                    buf = ""
            elif char == "]":
                out += choice[buf]
                buf = ""
            else:
                buf += char
        out += buf
        if mode == "task":
           task = out
           mode = "solution"
        elif mode == "solution":
           solution = out

    return task.capitalize(), solution.capitalize()

while True:
    task, solution = genrandomtask(data)
    print(task)
    input()
    print("Správná odpověď: {}\n".format(solution))
