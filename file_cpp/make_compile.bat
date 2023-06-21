@echo off
echo Compiling library code.....
g++ -c -o modules.o modules.cpp
ar rcs libmodules.a modules.o
ar rcs libmodules.lib modules.o
echo Setting up.....
mkdir static
move libmodules.lib ./static/libmodules.lib
move libmodules.a ./static/libmodules.a
echo Compiling and running program.....
g++ -o runner_cpp runner_cpp.cpp -O2 -I./ -L./static/ -lmodules
runner_cpp