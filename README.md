# test-simulator
[![CodeQL](https://github.com/Andrew1013-development/test-simulator/actions/workflows/codeql.yml/badge.svg)](https://github.com/Andrew1013-development/test-simulator/actions/workflows/codeql.yml) [![DevSkim](https://github.com/Andrew1013-development/test-simulator/actions/workflows/devskim.yml/badge.svg)](https://github.com/Andrew1013-development/test-simulator/actions/workflows/devskim.yml) [![OSSAR](https://github.com/Andrew1013-development/test-simulator/actions/workflows/ossar.yml/badge.svg)](https://github.com/Andrew1013-development/test-simulator/actions/workflows/ossar.yml)

## description
simulate sorting file by the first 8 characters of a filename as a date

## available languages:
- Python 3.9 -> 3.12
- C++20 (C++17 and C++23 in testing)

## test platforms:
- main codebase (all .py and .cpp / .hpp files):
  - Windows 11 build 25393.1 - Python 3.12.0b3 - g++ 13.1.0[^1]
  - Ubuntu 22.04.1 LTS (running via WSL2) - Python 3.10.6 (migrating to 3.10.11) - g++ 11.3.0[^1]
  - macOS Catalina 10.15.7 (19H15) - Python 3.11.4
  - Debian 11 (running via WSL2) - Python 3.9.17 - g++ 10.2.1[^1]

[^1]: tested with flags: -std=c++20 -march=native -flto (see in the Makefile in `file_cpp`)

## What you need to run this collection of scripts:
- Python 3.9.x to 3.12.x
- (optional) g++ 10.x to 13.x
- (optional) `make` or `mingw32-make`


## future improvements
- [x] plotting for C++ reimplementation
- [ ] telemetry for C++ reimplementation
- [ ] optimizations
- [ ] setup scripts
- [ ] wiki + proper documentation

## files and execution pipeline
[insert image of pipeline here]

## dont ask why is this place a thing
just a dude trying to find a hobby to pass the time during summer i guess?