import cv2
from .rules import *
from .loader import *
from .model_renderer import show, colorize, parse_palette, parse_sinks
from .osc import OSCSink, PrintSender
from argparse import ArgumentParser

parser = ArgumentParser(prog="Wireworld Composer", description="""
Compose sequences using wireworld simulations. Check the readme for details.
""")
parser.add_argument("config", help="path to the config file", type=str)
parser.add_argument("--windowsize", help="Resolution of the output animation, defaults to 512 pixels", type=int, default=512)
args = parser.parse_args()

data,world = load_file(args.config)
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
    show(colorize(config, field), (args.windowsize, args.windowsize))
    tick(field, output)
    cv2.waitKey(step)