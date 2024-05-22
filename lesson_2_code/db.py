import sqlite3

import sqlalchemy


def create():
    sqlite3.connect('lesson2.db')


def engine():
    return sqlalchemy.create_engine('sqlite:///lesson2.db')


def populate():
    # TODO use engine, CSVs and pandas to create and populate
    # 3 tables
    raise NotImplementedError

