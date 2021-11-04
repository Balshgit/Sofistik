# UI path 

    C:\Users\Balsh\AppData\Local\Programs\Python\Python39\Lib\site-packages\qt6_applications\Qt\bin\designer.exe

# Convert ui to py script

    python -m PyQt6.uic.pyuic -x sofistik.ui -o sofui.py

# Create exe
from git bash

    pyinstaller sofui.py

-F - creates one exe

-i - create app with icon /path/to/icon.ico

-w - create app without console

    pyinstaller -F -i icon.ico -w sofui.py
    
    

    




## Create migrations

Init alembic

    alembic init alembic

Create table in alembic versions
    
    alembic --config .\alembic\alembic.ini revision -m "create account table"

Run migrations

    cd .\sofistik\sofistik\database\ # alembic root
    alembic --config .\alembic\alembic.ini upgrade head

Downgrade migrations
    
    alembic --config .\alembic\alembic.ini downgrade 91fb76bc8019