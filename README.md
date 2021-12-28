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

- timeout per function
- more detailed report (excel format)
- synthesis (excel format)
- security against suspicious code
