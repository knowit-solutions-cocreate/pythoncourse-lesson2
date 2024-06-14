# Code for Python course lesson 2
Welcome to part two of the Python course!

The main topic of this part is how to integrate data-processing Python (and pandas) workflows with SQL workflows. As a sample database to work against, we will use SQLite. Secondary topics are Python project structure, package installation and command line interfacing.

Study plan suggestion:
1. Study the project code briefly by having a glimpse at all the files
2. Run the [project setup](#project-setup) steps
3. Do some or all of the [exercises](EXERCISES.md)
4. Have a look at [further reading](#further-reading)

Good luck!


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


## Further reading

### Connecting to "real" databases
The interaction between pandas and SQLite of the present code is handled by an "engine" object, see lesson_2_code/db.py. Initialization of an engine object for interaction with your production database of choice is generally a matter of driver installation, construction of a connection string and authentication. For Postgres, for example, drivers can be installed via the pip package psycopg2 and authentication provided directly in the connection string like so:
```Python
password = os.environ["edvardspostgres_pw"]  # store in environment variable to hide from code
engine = sqlalchemy.create_engine(f"postgresql+psycopg2://edvard:{password}@localhost:5432/edvardsdb")
```

Guides for connecting to various types of databases, including Microsoft SQL Server, can be found in the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/20/core/engines.html).

### Higher level tools for project setup
For simplicity, the present project uses the core tools `venv` and `pip` for management of virtual environment and dependencies. You will find that larger Python projects tend to delegate these tasks to higher level tools, such as [Poetry](https://python-poetry.org/). Some of the reasons are:
- to not have to explicitly create and activate the virtual environment
- to, in addition to the list of dependency version constraints (see setup.py), also maintain a "lock file" with exact versions to be able to more reliably reinstall them
- configurability of many development tools in a single project file
- ability to build and publish one's code with a single tool

### Publishing code
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) is a guide on how to publish a package to a remote package index. For making Python packages installable to colleagues, there are different options for hosting a protected package index. [Azure DevOps Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops) is one.
