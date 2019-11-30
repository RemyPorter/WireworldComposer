import cv2
from .rules import *
from .loader import *
from .model_renderer import show, colorize, parse_palette, parse_sinks

data,world = load_file("test_model.txt")
config = Config.parse_raw(data)


config.palette = parse_palette(config.palette)
config.sinks = parse_sinks(config.sinks)

field = parse_ascii(config, world)

step = int((1. / config.divisions) * 1000)

while True:
    show(colorize(config, field))
    tick(field)
    cv2.waitKey(step)