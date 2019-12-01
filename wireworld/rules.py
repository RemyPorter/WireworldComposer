"""Wire World Rules"""

import cv2
import numpy as np

from . import C, E, H, T, normalize

NEIGHBORHOOD = (
    np.array([-1, -1, -1,  0, 0,  1, 1, 1], np.int),
    np.array([-1,  0,  1, -1, 1, -1, 0, 1], np.int)
)
XS,YS = NEIGHBORHOOD

def fire_sink(x, y, sink, electrons, sender):
    """Output that a sink was triggered"""
    sender.send(sink,x,y,electrons)

def check_sinks(field, sender):
    """
    Check every sink to see if it has electrons as neighbors
    """
    size = field.shape[0]
    sx,sy = np.where(field > C)
    for x,y in zip(sx,sy):
        xq,yq = normalize(size, [x+XS,y+YS])
        neighbors = field[xq,yq]
        conds = np.where(neighbors == H)
        if (len(conds[0]) > 0):
            fire_sink(x, y, field[x,y], len(conds[0]), sender)

def check_conductors(field, pairs):
    """
    Check every conductor's x/y coordinate to
    see if its neighbors are electrons
    """
    nx,ny = [],[]
    size = field.shape[0]
    for x,y in zip(*pairs):
        xq,yq = normalize(size, [x+XS,y+YS])
        neighbors = field[xq,yq]
        conds = np.where(neighbors == H)
        cnt = len(conds[0])
        if cnt == 1 or cnt == 2:
            nx.append(x)
            ny.append(y)
    field[nx,ny] = H
        

def tick(field, sender):
    """Apply the wireworld state"""
    heads = np.where(field == H)
    tails = np.where(field == T)
    conductors = np.where(field == C)
    check_sinks(field, sender)
    check_conductors(field, conductors)
    field[heads] = T
    field[tails] = C
