@echo off
wsl "./run_essentia.sh" &
timeout 3
.\ABGvenv\Scripts\python.exe main.py
