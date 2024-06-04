# Code for Python course lesson 2

## Project setup

1. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) VSCode extensions
2. Create a virtual Python environment and activate it:
    ```console
    py -m venv venv
    .\venv\Scripts\activate
    ```
3. Install the Python code:
    ```console
    py -m pip install --editable ./
    ```
4. Setup the SQLite database:
    ```
    lesson2 db create
    lesson2 db populate
    ```
5. Open SQLite browser by opening lesson2.db in the VSCode file explorer
