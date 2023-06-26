CPP_FLAGS = -Wall -Wextra -O3 -std=c++20
MODULES_LIB = -L./shared -I./ -lmodules
ifeq ($(OS), Windows_NT)
	EXECUTABLE_EXTENSION = exe
	MAKE_CALL = mingw32-make
else	
	EXECUTABLE_EXTENSION = out
	MAKE_CALL = make
endif

.SILENT: all

all:
	echo Building dependencies.....
	g++ -c -o modules.o modules.cpp -libstdc++fs -fPIC $(CPP_FLAGS)
	
	g++ -shared -o shared/libmodules.so modules.o
	g++ -shared -o shared/libmodules.dll modules.o
	g++ -shared -o shared/libmodules.dylib modules.o
	echo Dependencies built.

	echo Compiling.....
	g++ -o runner_cpp.$(EXECUTABLE_EXTENSION) runner_cpp.cpp $(MODULES_LIB)  $(CPP_FLAGS)
	g++ -o sus_runner_cpp.$(EXECUTABLE_EXTENSION) sus_runner_cpp.cpp $(MODULES_LIB) $(CPP_FLAGS)
	g++ -o plotter_cpp.$(EXECUTABLE_EXTENSION) plotter_cpp.cpp $(MODULES_LIB) $(CPP_FLAGS)
	echo Compiled.