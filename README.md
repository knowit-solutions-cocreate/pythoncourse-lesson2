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

### Before you start
Familiarise yourself with reading from and writing to SQL using pandas by studying sql_read_example.py and sql_write_to_example.py. Try, for example, modifying sql_write_to_example.py, executing it with `py .\lesson_2_code\sql_write_to_example.py` then viewing the result in SQLite Viewer in VSCode.

You can always start over by deleting lesson2.db and recreating it using the instructions above.

### 1. Replace SQL-side join with a Python/pandas-side join
In lesson_2_code/populate_homeworlds_table.py there is a pure SQL-query which populates a table by combining the people information with that about their home planets.
Task: replace the SQL-side join with logic that loads the two tables into pandas dataframes, carries out the join using pandas then loads the result back using the `.to_sql` function.

Hints:
- how to read an SQL table into pandas is shown in sql_read_example.py
- how to write a pandas datafram into an SQL table is shown in sql_write_to_example.py
- in pandas, `.merge` is actually more similar to SQL's `JOIN` than `.join`

### 2. TODO A cleaning excercise
Task: TODO

Hints: TODO

### 3. TODO Perhaps another refinement exercise?
Task: TODO

Hints: TODO

### 4. Add new entries to a table using requests, an f-string-formatted query URL, dictionary lookup and a loop
Note that this is *hard*!

Task: TODO

Hints:
- TODO example code that queries a different swapi resource (perhaps films, because it's small), constructs a dataframe from the list of dicts then prints it


## Further reading

TODO cover
- Poetry
- Polars
- what connecting to a "more real" database e.g. PostreSQL or SQLServer may look like
- (maybe) typing
- anything that feels like a natural next learning step
