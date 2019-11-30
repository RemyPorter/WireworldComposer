"""Parse and load the config document"""
import json
from pydantic import BaseModel
from typing import List, Dict
import numpy as np
from . import H, C, T, E

def load_file(file):
    data = []
    world = []
    with open(file) as f:
        lines = f.readlines()
    in_header = True
    for l in lines:
        if in_header and l.startswith("-"):
            in_header = False
            continue
        if in_header:
            data.append(l)
        else:
            world.append(l)
    return "".join(data), "".join(world)

class Config(BaseModel):
    size:int
    divisions:int
    palette:List[str]
    sinks:Dict[str,str]={}

def parse_ascii(config, ascii):
    field = np.full((config.size, config.size), E)
    for x,l in enumerate(ascii.split("\n")):
        for y,c in enumerate(l):
            if c in "|+=-\\/_":
                field[x,y] = C
            elif c in "<>":
                field[x,y] = H
            elif c == "~":
                field[x,y] = T
            elif c == " ":
                field[x,y] = E
            else:
                field[x,y] = ord(c)
    return field


