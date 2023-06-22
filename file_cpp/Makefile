all:
	g++ -c -o modules.o modules.cpp -libstdc++fs -std=c++20 -fPIC
		
	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o

check:
	g++ -o runner_cpp.out runner_cpp.cpp -O3 -L./ -lmodules
ifeq ($(OS), Windows_NT)
	echo less gay
	runner_cpp.out
else
	echo more gay
	./runner_cpp.out
	endif