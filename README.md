# Code for Python course lesson 2

## Project setup

1. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) VSCode extensions
2. Create a virtual Python environment and activate it:
    ```console
    py -m venv venv
    .\venv\Scripts\activate  # run this step again whenever you open a new terminal
    ```
3. Select the Python interpreter within the virtual environment for VSCode to use: Ctrl+Shift+P, type "Python: Select Interpreter" and choose (or navigate to) .\venv\Scripts\python.exe
4. Install the Python code:
    ```console
    py -m pip install --editable ./
    ```
5. Setup the SQLite database:
    ```
    lesson2 db create
    lesson2 db populate
    ```
6. Open SQLite browser by opening lesson2.db in the VSCode file explorer
