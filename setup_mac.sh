#! /bin/bash
echo "test-simulator download script for Linux / macOS [PROTOTYPE]"
echo "test script only, not for production use yet"
echo $PWD
echo "Downloading on current directory....."
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_copier.py -o file_copier.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_seeker.py -o file_seeker.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_generator.py -o file_generator.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_remover.py -o file_remover.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_sorter.py -o file_sorter.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_sorter_2.py -o file_sorter_2.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_remover_2.py -o file_remover_2.py
curl https://raw.githubusercontent.com/Andrew1013-development/test-simulator/main/sys_fetcher.py -o sys_fetcher.py
curl https://raw.githubusercontent.com/Andrew1013-development/test-simulator/main/sys_uploader.py -o sys_uploader.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/sus_runner.py -o sus_runner.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/plotter.py -o plotter.py
curl https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/runner.py -o runner.py
curl -o logger.py
curl -o telemetry.py
echo "Done!"