import sqlite3
from contextlib import contextmanager
import logging

import sqlalchemy
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create(name='lesson2.db'):
    with connect(name):
        logger.info(f'creating {name}...')
        pass  # connecting and doing nothing implicitly creates it


@contextmanager
def connect(name='lesson2.db'):
    with sqlite3.connect(name) as connection:
        yield connection


def get_engine(name='lesson2.db'):
    return sqlalchemy.create_engine(f'sqlite:///{name}')


def populate(name='lesson2.db'):
    example_df = pd.DataFrame({'my_1st_col': [0, 1], 'my_2nd_col': [3, 4]})
    people_df = pd.read_csv('data/people.csv')
    planets_df = pd.read_csv('data/planets.csv')

    logger.info(f'populating three {name} tables...')
    db_engine = get_engine()
    example_df.to_sql('example', db_engine, if_exists="replace", index=False)
    people_df.to_sql('people', db_engine, if_exists="replace", index=False)
    planets_df.to_sql('planets', db_engine, if_exists="replace", index=False)
