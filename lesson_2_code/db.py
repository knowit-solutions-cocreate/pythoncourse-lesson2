import sqlite3
from contextlib import contextmanager

import sqlalchemy
import pandas as pd


def create():
    with connect():
        pass  # connecting and doing nothing implicitly creates it


@contextmanager
def connect():
    with sqlite3.connect('lesson2.db') as connection:
        yield connection


def get_engine():
    return sqlalchemy.create_engine('sqlite:///lesson2.db')


def populate():
    example_df = pd.DataFrame({'my_1st_col': [0, 1], 'my_2nd_col': [3, 4]})
    people_df = pd.read_csv('data/people.csv')
    planets_df = pd.read_csv('data/planets.csv')

    db_engine = get_engine()
    example_df.to_sql('example', db_engine, if_exists="replace", index=False)
    people_df.to_sql('people', db_engine, if_exists="replace", index=False)
    planets_df.to_sql('planets', db_engine, if_exists="replace", index=False)
    # TODO create joined version here?
