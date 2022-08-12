# AtmosphericBG

AtmosphericBG is a senior project created by Rodney Chan, Devin Salter,Tony Lei, and Minh Quach.
The main purpose of AtmosphericBG is to change your desktop background and the color of led light strip by analyzing genre of music.
For example, if you are playing classical music, the background will change to a theme that matches classical music.
Background pictures selected by the program can be manually set or they can be dynamically generated.
There will also be extra features. The dynamic app theme change can change the color of the app itself based off the musical analysis.
The visualizer is another tool that shows the sound waves of the song in real time.

##Step 1:	Install Python 3.10.5 in Windows environment

##Step 2: Install Git Bash

##Step 3: Set up Windows Python venv
	cd ...\AtmosphericBG
	git submodule update --init
	python -m venv ABGvenv
	activate_venv.bat
	pip install -r requirements.txt


##Step 4: Enable WSL and install Ubuntu
	Open Control Panel -> Programs and Features -> Turn Windows Feature on or off -> Check Windows Subsystem for Linux
	Install Ubuntu from the Microsoft Store, set up environment account during installation

##Step 5: Set up WSL environment
	sudo apt upgrade
	sudo apt-get update
	sudo apt install python3-pip
	pip install essentia
	pip install tensorflow
	pip install essentia-tensorflow
	sudo apt-get install libsndfile1
	sudo apt-get install libportaudio2
	sudo apt-get install -y python3-opencv
	sudo apt-get install libgl1
	sudo apt install libxkbcommon-x11-0
	sudo apt install libxcb-xinerama0
	sudo apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
	sudo apt-get install build-essential libeigen3-dev libyaml-dev libfftw3-dev libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libsamplerate0-dev libtag1-dev libchromaprint-dev
	sudo apt-get install python3-dev python3-numpy-dev python3-numpy python3-yaml python3-six

At this point, extract the essentia folder from essentia.rar
	cd essentia/packaging
	./build_3rdparty_static_debian.sh
	python3 waf configure --build-static --with-python --with-cpptests --with-examples --with-vamp
	python3 waf
	sudo python3 waf install

##Step 6: Run the application
###	NOTES: Running the application currently relies upon having two open console windows
###		   essentia_main.py must be running before run_program.bat is used, else the program will fail to open

	Open Ubuntu.exe
	cd .../AtmosphericBG
	python3 essentia_main.py

	Open cmd.exe
	cd ...\AtmosphericBG
	run_program.bat
