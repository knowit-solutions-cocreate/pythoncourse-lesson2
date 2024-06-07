# Code for Python course lesson 2
Welcome to part two of the Python course!

The main topic of this part is how to integrate data-processing Python (and pandas) workflows with SQL workflows. As a sample database to work against, we will use SQLite. Secondary topics are Python project structure, package installation and command line interfacing.


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
    ```console
    lesson2 db create
    lesson2 db populate
    ```
6. Open SQLite browser by opening lesson2.db in the VSCode file explorer


## Excercises

1. Task: TODO
   Tips: TODO
2. TODO
3. ...


## Further reading

TODO cover
- TODO make list
- ...
