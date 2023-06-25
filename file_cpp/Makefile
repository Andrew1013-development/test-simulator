CPP_FLAGS = -Wall -Wextra -O3 -std=c++20
ifeq ($(OS), Windows_NT)
	EXECUTABLE_EXTENSION = exe
else	
	EXECUTABLE_EXTENSION = out
endif

.SILENT: all

all:
	g++ -c -o modules.o modules.cpp -libstdc++fs -fPIC $(CPP_FLAGS)
	
	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o
	
	g++ -o runner_cpp.$(EXECUTABLE_EXTENSION) runner_cpp.cpp  -L./ -lmodules -Wl,-rpath=./ $(CPP_FLAGS)
	g++ -o sus_runner_cpp.$(EXECUTABLE_EXTENSION) sus_runner_cpp.cpp -L./ -lmodules -Wl,-rpath=./ $(CPP_FLAGS)