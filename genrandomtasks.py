#!/usr/bin/env python3

import sys
import yaml
import random

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

def main(argv):
    if len(argv) != 2:
        print("Usage: {} data.yaml".format(argv[0]))
        exit(64)

    with open(argv[1], 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    while True:
        try:
            task, solution = genrandomtask(data)
            print(task)
            inp = input()
            print("Správná odpověď: {}\n".format(solution))
            if inp != "": quit()
        except KeyboardInterrupt:
            quit()

if __name__ == "__main__":
   main(sys.argv)
