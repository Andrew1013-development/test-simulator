ifeq ($(OS), Windows_NT)
	EXECUTABLE_EXTENSION = exe
else	
	EXECUTABLE_EXTENSION = out
endif

all:
	g++ -c -o modules.o modules.cpp -libstdc++fs -std=c++20 -fPIC -Wall -Wextra
	
	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o
	
	g++ -o runner_cpp.$(EXECUTABLE_EXTENSION) runner_cpp.cpp -O3 -L./ -lmodules -Wl,-rpath=./ -Wall -Wextra
	g++ -o sus_runner_cpp.$(EXECUTABLE_EXTENSION) sus_runner_cpp.cpp -O3 -L./ -lmodules -Wl,-rpath=./ -Wall -Wextra