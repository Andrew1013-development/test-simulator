@echo off
cd %~dp0
echo %~dp0

:setup
echo %1
echo %2
echo %3
echo %4 

:clearing_old
echo Clearing up old executables and object code.....
:: delete old object code and executables
for %%f in (*.o) do del %%f
for %%f in (*.exe) do del %%f

:make_compile
echo Compiling library code.....
g++ -c -o modules.o modules.cpp
ar rcs libmodules.a modules.o
ar rcs libmodules.lib modules.o
echo Setting up.....
mkdir static
move libmodules.lib ./static/libmodules.lib
move libmodules.a ./static/libmodules.a
echo Compiling and running program.....
@echo on
g++ -o runner_cpp runner_cpp.cpp -O3 -I./ -L./static/ -lmodules
runner_cpp %1 %2 %3 %4