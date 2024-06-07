import sqlite3

import sqlalchemy
import pandas as pd


def create():
    sqlite3.connect('lesson2.db')


def get_engine():
    return sqlalchemy.create_engine('sqlite:///lesson2.db')


def populate():
    db_engine = get_engine()

    people_df = pd.read_csv('data/people.csv')
    planets_df = pd.read_csv('data/planets.csv')

    people_df.to_sql('people', db_engine, if_exists="replace", index=False)
    planets_df.to_sql('planets', db_engine, if_exists="replace", index=False)
    # TODO create joined version here?
