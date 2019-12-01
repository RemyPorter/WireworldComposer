"""Parse and load the config document"""
import json
from pydantic import BaseModel
from typing import List, Dict, Union
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

class OscConfig(BaseModel):
    host:str = "localhost"
    port:int = 8481
    addr:str = "/wireworld"

class PrintConfig(BaseModel):
    debug:bool = True

class Timing(BaseModel):
    bpm:int=120
    subdivisions:int=16

class Config(BaseModel):
    size:int
    palette:List[str]
    sinks:Dict[str,str]={}
    tempo:Timing=Timing()
    osc:Union[OscConfig, PrintConfig] = PrintConfig()

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


