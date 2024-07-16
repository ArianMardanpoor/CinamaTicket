#! usr/bin/python3
import argparse
import json


parser = argparse.ArgumentParser(description="Definition of film specifications...")

parser.add_argument("--Movie", type=str, required=True)
parser.add_argument("--ages", type=int)
parser.add_argument("--Capacity", type=int)

args = parser.parse_args()
arguments = parser.parse_args()


with open('args.json', 'w') as f:
        json.dump(vars(args), f)

