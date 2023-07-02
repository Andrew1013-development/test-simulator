CPP_FLAGS = -Wall -Wextra -O3 -std=c++20 -march=native -flto
MODULES_LIB = -L./ -I./ -lmodules
VERSION = 1.0.0
#Linux vs Windows config shit
ifeq ($(OS), Windows_NT)
	EXECUTABLE_EXTENSION = exe
	MAKE_CALL = mingw32-make
	COPY_CMD = copy
	MOVE_CMD = move
	LIST_DIR = dir
else
	EXECUTABLE_EXTENSION = out
	MAKE_CALL = make
	COPY_CMD = cp
	MOVE_CMD = mv
	LIST_DIR = ls
endif

all:
	@echo Building library.....
	g++ -c -o modules.o modules.cpp -libstdc++fs -fPIC $(CPP_FLAGS)
	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o
	@echo Library built.

	@echo Compiling.....
	g++ -o runner_cpp.$(EXECUTABLE_EXTENSION) runner_cpp.cpp $(MODULES_LIB)  $(CPP_FLAGS)
	g++ -o sus_runner_cpp.$(EXECUTABLE_EXTENSION) sus_runner_cpp.cpp $(MODULES_LIB) $(CPP_FLAGS)
	@echo Compiled.
	
plotter:
	@echo Copying to file_py.....
	$(COPY_CMD) sus_runner_cpp.$(EXECUTABLE_EXTENSION) ..\file_py\sus_runner_cpp.$(EXECUTABLE_EXTENSION)
	$(COPY_CMD) libmodules.so ..\file_py\libmodules.so
	$(COPY_CMD) libmodules.dll ..\file_py\libmodules.dll
	$(COPY_CMD) libmodules.dylib ..\file_py\libmodules.dylib
	@echo Copied to file_py.

version:
	@echo Current version: $(VERSION)