#!/usr/bin/python
import os
import subprocess

print("start")

os.system("chmod +rwx -v ./start.sh")
subprocess.call(['sh', './start.sh'])

os.system("chmod +rwx -v ./Nubot-code/run.py")
os.chdir('Nubot-code')

key = 'TOKEN'
value = os.getenv('TOKEN')
print("Value of 'TOKEN' environment variable :", value) 

pip install ffmpeg-python
os.system('python run.py')
print("end")
