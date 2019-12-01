# Wireworld Composer
For Python 3.6+.

This is a [wireworld](https://en.wikipedia.org/wiki/Wireworld) simulator with hooks to send messages via a variety of protocols (to be implemented- currently it just dumps output to the console). The idea is that it will run as a controller for audio systems, allowing you to program complex triggers via Wireworld automata.

## Use
```
usage: Wireworld Composer [-h] [--windowsize WINDOWSIZE] config

Compose sequences using wireworld simulations. Check the readme for details.

positional arguments:
  config                path to the config file

optional arguments:
  -h, --help            show this help message and exit
  --windowsize WINDOWSIZE
                        Resolution of the output animation, defaults to 512
                        pixels
```

### File Format
The TXT file format has two sections: a JSON snipped which configures
key elements of the environment, and an ASCII art block describing the wireworld.

#### JSON Section
* Size: how many cells square the simulation should be
* palette: should contain 4 entries, which are the colors for Empty, Head, Tail, and Conductor cells in order. Hex colors.
* sinks: a dictionary mapping a character to a color. The keys should all be one character in size, and should be an ASCII character. They should not be one of the characters reserved for ASCII art, they should not be a weird control character. This color will be used to draw the sinks in the simulation.
* osc: map the output. Either use a single boolean key, `debug` (its value doesn't matter, but should probably be `true` just for sanity), or supply a `host`/`port` and OSC `addr` (with the leading `/`)
* tempo: supply a `bpm` and a number of `subdivisions`. This controls the timing/framerate

#### ASCII Art Section
A separator line (starting with `-`) marks the end of the JSON block. The following block is the wireworld simulation we want to run as ASCII art. I recommend using [AsciiFlow](http://asciiflow.com/) to draw it.

The ASCII art language works thus:

* Conductors: any one of `|+=-\/_`
* Electron Heads: either `<` or `>`
* Electron tails: `~`
* Empty cells: ` `
* Sinks: any ASCII character with an ordinal greater than 3, e.g. don't use weird control characters. NB: the same sink can appear multiple times in the diagram. They are effectively the same sink, and any OSC messages they trigger go to the same place.

## OSC Output
The `addr` property of the OSC output is the base address to which all OSC messages will be sent. The default address is `/wireworld`. This is the *base address*. Each sink will have its own address. As you add a sink to the ASCII art diagram, they will each have their own sub-address based on their character, e.g., the sink `c` will send data to `/wireworld/c`.

The content of the message will be the `[x, y, count]`- the x/y coordinates of the sink and the number of electrons that were triggering the message.