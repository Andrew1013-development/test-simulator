# test-simulator
## description
simulate sorting file by the first 8 characters of a filename as a date

## test platforms
- main codebase (all .py files):
  - Windows 11 build 25393.1 - Python 3.12.0b2 - g++ 13.1.0
  - Ubuntu 22.04.1 LTS (running via WSL2) - Python 3.10.6 - g++ 11.3.0
  - macOS Catalina 10.15.7 (19H15) - Python 3.11.4
  - Debian 11 (running via WSL2) - Python 3.9.17 - g++ 10.2.1

## What you need to run this collection of scripts:
- Python 3.12 / 3.11 / 3.10 / 3.9
- (optional) g++ 10.0 / 11.0 / 12.0 / 13.0
- (optional) make

## How to setup and run:
- Clone straight from GitHub
  - `git clone https://github.com/Andrew1013-development/test-simulator.git` - HTTPS cloning (recommended)
  - `git clone git@github.com:Andrew1013-development/test-simulator.git` - SSH cloning (only for SSH authorized machine)
  - Code -> Download as ZIP -> extract to desired folder
- Change into the cloned folder
  - Navigate to folder
  - `cd {folder_directory}`
- `pip install -r requirement.txt` - install dependencies for plotter.py and runner.py
- run either runner.py or plotter.py script 
  - all files with "file_" / "sys_" prefixes or bearing the names "modules" are functions / modules files only, not for running code directly
  - specify arguments in command (5 for plotter.py, 4 for runner.py): 
    - Example 1 (plotter.py): `python3 plotter.py Z:\test-simulator\test1 -nodebug -nofulldebug 15 -file` 
    - Example 2 (plotter.py): `python3 plotter.py help`
    - Example 3 (runner.py): `python3 runner.py test1 -debug -fulldebug 6 -file`
    - Example 4 (runner.py): `python3 runner.py help`

## future improvements
## files and execution pipeline
[insert image of pipeline here]

## dont ask why is this place a thing
