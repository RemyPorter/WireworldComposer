import cv2
from .rules import *
from .loader import *
from .model_renderer import show, colorize, parse_palette, parse_sinks
from .osc import OSCSink, PrintSender

data,world = load_file("test_model.txt")
config = Config.parse_raw(data)


config.palette = parse_palette(config.palette)
config.sinks = parse_sinks(config.sinks)

if isinstance(config.osc, OscConfig):
    output = OSCSink(config.osc)
else:
    output = PrintSender(config.osc)
output.start()

field = parse_ascii(config, world)

step = int((60. / (config.tempo.bpm * config.tempo.subdivisions)) * 1000)

while True:
    show(colorize(config, field))
    tick(field, output)
    cv2.waitKey(step)