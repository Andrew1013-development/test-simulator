all:
	g++ -c -o modules.o modules.cpp -libstdc++fs -std=c++20 -fPIC
		
	g++ -shared -o modules.so modules.o
	g++ -shared -o modules.dll modules.o
	g++ -shared -o modules.dylib modules.o

check:
	g++ -o runner_cpp.out runner_cpp.cpp -O3 -L./ -lmodules
	runner_cpp.out