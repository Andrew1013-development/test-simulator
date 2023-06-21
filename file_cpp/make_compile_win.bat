@echo off
cd %~dp0

echo Clearing up old executables and object code.....
:: delete old object code and executables
for %%f in (*.o) do del %%f
for %%f in (*.exe) do del %%f

echo Compiling library code.....
g++ -c -o modules.o modules.cpp
ar rcs libmodules.lib modules.o
echo Setting up.....
mkdir static
move libmodules.lib ./static/libmodules.lib
echo Compiling and running program.....
g++ -o runner_cpp runner_cpp.cpp -O3 -I./ -L./static/ -lmodules
runner_cpp %1 %2 %3 %4