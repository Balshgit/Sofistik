# UI path 

    C:\Users\Balsh\AppData\Local\Programs\Python\Python39\Lib\site-packages\qt6_applications\Qt\bin\designer.exe

# Convert ui to py script

    python -m PyQt6.uic.pyuic -x sofistik.ui -o sofui.py

# Create exe
from git bash

    pyinstaller sofui.py