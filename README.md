# PyCorrector

PyCorrector is a small python application that has for objective to grade a large amount of student's python code.
PyCorrector goals are
- fast and reliable student's code grading
- flexible grading functions

## Installation

Made with Python 3.8.10 but most of python 3.X versions should work

All dependencies can be obtained by the following commands
```sh
python3 -m pip install -r requirements.txt
```
Once that's done, everything should be working !

## Usage

First move all compressed students code files(.zip/.tar.gz/.7z supported) into the studentFiles folder

Then, from the project root directory execute
```sh
python3 Corrector.py
```
A ratings.txt file will be generated with a grade for each student's compressed file.

## TODO

- ~~Timeout per function~~
- ~~Better auto-update~~
- multiple input test for the same function
- ~~static var in config file~~
- More detailed report (excel format)
- Synthesis (excel format)
- visual interface for config
- ~~Security against suspicious code~~
- Cheat detection
