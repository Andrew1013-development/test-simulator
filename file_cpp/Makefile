all:
	g++ -c -o modules.o modules.cpp -libstdc++fs -std=c++20 -fPIC
		
	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o

check:
	g++ -o runner_cpp.out runner_cpp.cpp -O3 -L./ -lmodules -Wl,-rpath=./
ifeq ($(OS), Windows_NT)
	runner_cpp.out
else
	./runner_cpp.out
endif
