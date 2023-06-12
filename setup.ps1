Write-Host "test-simulator download script for Windows [PROTOTYPE]"
Write-Host "test script only, not for production use yet"
Write-Host $pwd
Write-Host "Downloading on current directory....."
Invoke-WebRequest "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_copier.py" -OutFile file_copier.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_seeker.py" -OutFile file_seeker.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_generator.py" -OutFile file_generator.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_remover.py" -OutFile file_remover.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_sorter.py" -OutFile file_sorter.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_sorter_2.py" -OutFile file_sorter_2.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/file_remover_2.py" -OutFile file_remover_2.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/sus_runner.py" -OutFile sus_runner.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/plotter.py" -OutFile plotter.py
Invoke-WebRequest -URI "https://raw.githubusercontent.com/Andrew1013-development/python-tester/main/runner.py" -OutFile runner.py
Write-Host "Done!"