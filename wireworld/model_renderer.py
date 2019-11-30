"""Methods to handle colors and rendering of wireworld objects"""
import cv2
import numpy as np
from webcolors import hex_to_rgb

from . import C, E, H, T, normalize

def parse_palette(colors):
    """Parse the palette to RGB arrays"""
    return [
        hex_to_rgb(c) for c in colors
    ]

def parse_sinks(colors):
    """Parse the sink colors into RGB arrays"""
    return {
        k: hex_to_rgb(c) for k,c in colors.items()
    }

def colorize(world, field):
    """Apply both the palettes and the sinks to colorize the image"""
    frame = np.zeros((world.size,world.size,3), np.ubyte)
    for i,c in enumerate(world.palette):
        frame[np.where(field==i)] = c
    for s,c in world.sinks.items():
        frame[np.where(field==ord(s))] = c
    return frame

def show(frame, size=(512,512)):
    """Show the image"""
    frame = cv2.resize(frame, size, interpolation=cv2.INTER_NEAREST)
    cv2.imshow("test", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
