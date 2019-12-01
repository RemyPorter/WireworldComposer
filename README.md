# Wireworld Composer
This is a [wireworld](https://en.wikipedia.org/wiki/Wireworld) simulator with hooks to send messages via a variety of protocols (to be implemented- currently it just dumps output to the console). The idea is that it will run as a controller for audio systems, allowing you to program complex triggers via Wireworld automata.

## Use
Right now, all the key data is stored in `test_model.txt`. Nothing takes any parameters, so simply run `python -m wireworld`, and it will render a test animation while printing out when the single sink gets triggered.

### File Format
The TXT file format has two sections: a JSON snipped which configures
key elements of the environment, and an ASCII art block describing the wireworld.

#### JSON Section
* Size: how many cells square the simulation should be
* palette: should contain 4 entries, which are the colors for Empty, Head, Tail, and Conductor cells in order. Hex colors.
* sinks: a dictionary mapping a character to a color. The keys should all be one character in size, and should be an ASCII character. They should not be one of the characters reserved for ASCII art, they should not be a weird control character. This color will be used to draw the sinks in the simulation.
* osc: map the output. Either use a single boolean key, `debug` (its value doesn't matter, but should probably be `true` just for sanity), or supply a host/port and OSC addr (with the leading `/`)
* tempo: supply a `bpm` and a number of `subdivisions`. This controls the timing/framerate

#### ASCII Art Section
A separator line (starting with `-`) marks the end of the JSON block. The following block is the wireworld simulation we want to run as ASCII art. I recommend using [AsciiFlow](http://asciiflow.com/) to draw it.

The ASCII art language works thus:

* Conductors: any one of `|+=-\/_`
* Electron Heads: either `<` or `>`
* Electron tails: `~`
* Empty cells: ` `
* Sinks: any ASCII character with an ordinal greater than 3, e.g. don't use weird control characters.