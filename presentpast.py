import yaml
import random
import re

with open("presentpast.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def genrandomtask(data):
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
           task = out.capitalize()
           mode = "solution"
        elif mode == "solution":
           solution = out.capitalize()

    return task, solution

def quit():
    print("\nDěkujeme za použití programu.")
    exit(0)

while True:
    try:
        task, solution = genrandomtask(data)
        print(task)
        inp = input()
        print("Správná odpověď: {}\n".format(solution))
        if inp != "": quit()
    except KeyboardInterrupt:
        quit()
