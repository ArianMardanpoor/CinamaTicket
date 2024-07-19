#! usr/bin/python3
import argparse
import json

mov = []

with open('cinama/cinama.json', 'r') as u:
    mov = json.load(u)

parser = argparse.ArgumentParser(description="Definition of film specifications...")

parser.add_argument("--movie", type=str, required=True)
parser.add_argument("--ages", type=int, required=True)
parser.add_argument("--capacity", type=int, required=True)
parser.add_argument("--price", type=int, required=True)

args = parser.parse_args()
arguments = parser.parse_args()
mov.append(vars(args))

with open('cinama/cinama.json', 'w') as f:
    json.dump(mov, f)

