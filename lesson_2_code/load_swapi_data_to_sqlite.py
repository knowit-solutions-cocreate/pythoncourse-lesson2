#!/usr/bin/env python
"""
"""
import sqlite3
import pandas as pd
from pathlib import Path


PEOPLE_CSV_PATH = Path("./data/people.csv")
PLANETS_CSV_PATH = Path("./data/planets.csv")


def load_people_csv(conn, people_csv_path):
    people_df = pd.read_csv(people_csv_path)
    people_df.to_sql("people", conn, if_exists="replace", index=False)


def load_planets_csv(conn, planets_csv_path):
    planets_df = pd.read_csv(planets_csv_path)
    planets_df.to_sql("planets", conn, if_exists="replace", index=False)


def join_into_table(conn):

    sql = """
    SELECT
      p.name AS name,
      pl.name AS planet_name,
      pl.terrain AS terrain,
      pl.climate AS climate,
      pl.gravity AS gravity
    FROM people p
    LEFT JOIN planets pl ON p.homeworld = pl.url;
    """

    joined_df = pd.read_sql_query(sql, conn)
    joined_df.to_sql("people_homeworlds", conn, if_exists="replace", index=False)


def main():
    with sqlite3.connect("swapi.db") as conn:
        load_people_csv(conn, PEOPLE_CSV_PATH)
        load_planets_csv(conn, PLANETS_CSV_PATH)

        join_into_table(conn)


if __name__ == "__main__":
    main()
