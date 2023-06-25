@echo off

set /p n_iters="enter amount of folders: "
set /p path1="enter path 1:"
set /p path2="enter path 2:"
set /p path3="enter path 3:"

for /l %%i in (1,1,%n_iters%) do (
    cd file_py
    python3 sus_runner.py %path1% %path2% %path3% -nodebug -nofulldebug %%i  
    cd ..\file_cpp
    mingw32-make
    runner_cpp.exe %path3% -nodebug -nofulldebug %%i
    cd ..
)