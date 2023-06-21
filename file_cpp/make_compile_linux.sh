#! /usr/bin/bash
cd $PWD

echo Clearing up old executables and object code.....
rm *.o

echo $1
echo $2
echo $3
echo $4

echo Compiling library code.....
g++ -c -o modules.o modules.cpp -libstdc++fs -std=c++20
ar rcs libmodules.a modules.o
echo Setting up.....
mkdir static
mv libmodules.a static
echo Compiling program.....
g++ -o runner_cpp runner_cpp.cpp -O3 -I./ -L./static/ -lmodules
echo Running program.....
./runner_cpp ~/test-simulator/test_cpp -nodebug -nofulldebug 1

