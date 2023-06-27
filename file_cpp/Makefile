CPP_FLAGS = -Wall -Wextra -O3 -std=c++20
MODULES_LIB = -L./ -I./ -lmodules
MODULES_DIR = shared
IMGUI_DIR = dependencies/imgui
SDL_DIR = dependencies/SDL
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

	g++ -shared -o libmodules.so modules.o
	g++ -shared -o libmodules.dll modules.o
	g++ -shared -o libmodules.dylib modules.o
	echo Dependencies built.

	echo Compiling.....
	g++ -o runner_cpp.$(EXECUTABLE_EXTENSION) runner_cpp.cpp $(MODULES_LIB)  $(CPP_FLAGS)
	g++ -o sus_runner_cpp.$(EXECUTABLE_EXTENSION) sus_runner_cpp.cpp $(MODULES_LIB) $(CPP_FLAGS)
	g++ -o plotter_cpp.$(EXECUTABLE_EXTENSION) plotter_cpp.cpp $(MODULES_LIB) $(CPP_FLAGS)
	g++ -o plotter_cpp.exe plotter_cpp.cpp dependencies/imgui/backends/imgui_impl_sdl2.cpp dependencies/imgui/backends/imgui_impl_opengl3.cpp dependencies/imgui/imgui*.cpp -I./dependencies -L./ -I./dependencies/SDL -lSDL2 -lmodules -I./dependencies/SDL/include
	echo Compiled.