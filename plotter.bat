@echo off
python3 plotter.py Z:\test-simulator\test -nodebug -nofulldebug 5 -file
copy runtime_stats.csv %userprofile%\desktop\runtime_stats.csv