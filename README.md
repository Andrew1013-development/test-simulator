# test-simulator
## description
simulate sorting file by the first 8 characters of a filename as a date

## testing
- main codebase (all .py files):
  - Windows 11 build 25393.1 - Python 3.12.0b2
  - Ubuntu 22.04.1 LTS (running via WSL2) - Python 3.10.6
  - macOS Catalina 10.15.7 (19H15) - Python 3.11.4
  - Debian 11 (running via WSL2) - Python 3.9.17
- main codebase C++ reimplementation (all .cpp + .hpp files)
  - Windows 11 build 25393.1 - g++ 13.1.0
  - Ubuntu 22.04.1 LTS (running via WSL2) - g++ 11.3.0
**- setup files (listed individually):
  - setup_win.ps1:
    - Windows 11 build 25393.1
    - PowerShell 5.1.25387.1
  - setup_mac.sh:
    - macOS 11.7.7 Big Sur
    - Bash 3.2.57(1)-release
  - setup_linux.sh:
    - Windows 11 build 25393.1 with WSL2 1.2.5.0
    - Ububtu 22.04.1 LTS / Debian 11(kernel version 5.15.90.1)
    - Bash 5.1.16(1)-release / Bash 5.1.4(1)-release**
## how to setup
What you need to run this collection of scripts:
- Python 3.12 / 3.11 / 3.10 / 3.9
- one of the setup scripts for your platform / Git Bash
How to run:
- Clone straight from GitHub
  - `git clone https://github.com/Andrew1013-development/test-simulator.git` - HTTPS cloning (recommended)
  - `git clone git@github.com:Andrew1013-development/test-simulator.git` - SSH cloning (only for SSH authorized machine)
  - Code -> Download as ZIP -> extract to desired folder
- ~~Option 2: download and run the setup_{platform} scripts:~~ ***do not use Option 2, setup files aren't updated yet.***
  - ~~`bash setup_linux.sh`~~
  - ~~`bash setup_mac.sh`~~
  - ~~`powershell setup_win.ps1`~~
- Change into the cloned folder
  - Navigate to folder
  - `cd {folder_name}` or `cd {folder_directory}`
- `pip install -r requirement.txt` - install dependencies for plotter.py and runner.py
  - if matplotlib fails to install, ignore
- run either runner.py or plotter.py script 
  - all files with "file_" / "sys_" prefixes are function files only, not for running code directly
  - specify arguments in command: 
    - Example 1 (plotter.py): `python3 plotter.py Z:\test-simulator\test1 -nodebug -nofulldebug 15 -file` 
    - Example 2 (plotter.py): `python3 plotter.py help`
    - Example 3 (runner.py): `python3 runner.py test1 -debug -fulldebug 6 -file`
    - Example 4 (runner.py): `python3 runner.py help`

## files and execution pipeline
[insert image of pipeline here]

## dont ask why is this place a thing
