import sqlite3
import pandas as pd


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
        join_into_table(conn)


if __name__ == "__main__":
    main()
