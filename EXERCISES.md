# Excercises

## Before you start
Familiarise yourself with reading from and writing to SQL using pandas by studying sql_read_example.py and sql_write_to_example.py. Try, for example, modifying sql_write_to_example.py, executing it with `py .\lesson_2_code\sql_write_to_example.py` then viewing the result in SQLite Viewer in VSCode.

You can always start over by deleting lesson2.db and recreating it using the instructions above.


## Main exercises

### 1. Replace SQL-side join with a Python/pandas-side join
In lesson_2_code/populate_homeworlds_table.py there is a pure SQL-query which populates a table by combining the people information with that about their home planets.

Task: replace the SQL-side join with logic that loads the two tables into pandas dataframes, carries out the join using pandas then loads the result back using the `.to_sql` function. Drop columns whose elements contain URLs or lists of URLs. Keep the rest of the columns.

Hints:
- how to read an SQL table into pandas is shown in sql_read_example.py
- how to write a pandas datafram into an SQL table is shown in sql_write_to_example.py
- in pandas, `.merge` is actually more similar to SQL's `JOIN` than `.join`

### 2. Data cleaning
Upon inspecting the homeworlds table you should find that there are a few issues when it comes to data representation. For example, some columns represent some missing values with NULL and others with "none", and some columns are stored with strings despite the information being numeric.

We suggest implementing all steps of this exercise in the same file. You could start by copying the contents of sql_read_example.py to a new file called clean_homeworlds.py.

#### a. Properly represent missing values
Task: replace NULL-representing strings such as "unknown" and "none" with values that translate to proper NULLs in the database.

Hints: pandas provides multiple functionalities that help with this. `.replace` and `.where` are two examples.

#### b. Represent height as integer
Task: convert the string representation of the height column to int.

Hints: the convenience function `pd.to_numeric` usually does what you want in this context. Have a look at its documentation.

#### c. Represent mass and birth_year as float
Task: convert the string representations of the mass and birth_year columns to float.

Hints: This is trickier than b because a little bit of string-preprocessing is required before `pd.to_numeric` will work. Namely, there is a decimal comma that needs to replaced with a regular decimal dot and a "BBY" (short for "Before the Battle of Yavin", apparently) substring that needs to be removed. In pandas, you can access convenience string manipulation functions in the `pd.Series.str` property: try typing `df["mass"].str.` into VSCode and scroll through the suggestions to find what you need.

#### d. Save the result in a new table
Task: save the result of applying all the three cleaning procedures to a new table.

Hints: lesson_2_code/sql_write_to_example.py.

### 3. Add new entries to a table using requests, an f-string-formatted query URL, dictionary lookup and a loop
Note that this is *hard*!

Task: TODO

Hints:
- TODO example code that queries a different swapi resource (perhaps films, because it's small), constructs a dataframe from the list of dicts then prints it


## Bonus exercises

- TODO CLI operation
- TODO publish package
- TODO any more?