# python-tester
## description
simulate sorting file by the first 8 characters of a filename as a date

## testing
- main codebase (all .py files):
  - Windows 11 build 25387.1200 - Python 3.12.0b2
  - Ubuntu 22.04.1 LTS (running via WSL2) - Python 3.10.6
  - macOS Catalina 10.15.7 (19H15) - Python 3.11.4
- setup files (listed individually):
  - setup_win.ps1:
    - Windows 11 build 25387.1200
    - PowerShell 5.1.25387.1
  - setup_mac.sh:
    - macOS 10.15.7 Catalina (19H15)
    - Bash 3.2.57(1)-release
  - setup_linux.sh:
    - Windows 11 build 25387.1200
    - WSL2 1.2.5.0
    - Ububtu 22.04.1 LTS (kernel version 5.15.90.1)
    - Bash 5.1.16(1)-release  

## how to setup
What you need to run this collection of scripts:
- Python 3.12 / 3.11 / 3.10
- one of the setup scripts for your platform / Git Bash
How to run:
- Option 1: clone straight from GitHub
  - `git clone https://github.com/Andrew1013-development/test-simulator.git` - HTTPS cloning (recommended)
  - `git clone git@github.com:Andrew1013-development/test-simulator.git` - SSH cloning (only for SSH authorized machine)
  - "Download as ZIP"
- Option 2: download and run the setup_{platform} scripts:
  - `bash setup_linux.sh`
  - `bash setup_mac.sh`
  - `powershell setup_win.ps1` 
- `pip install plotly rich matplotlib` - install dependencies for plotter.py and runner.py
  - if matplotlib fails to install, ignore
- run the sus_runner.py / runner.py / plotter.py scripts 
  - all files with "file_" prefixes are function files only, not for running code directly 
## files and pipeline
[insert image of pipeline here]

## dont ask why is this place a thing
