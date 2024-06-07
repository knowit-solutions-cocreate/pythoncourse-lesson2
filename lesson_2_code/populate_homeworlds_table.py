import pandas as pd

import db


def join_into_table(connection):
    creation_query = """
    CREATE TABLE homeworlds(
      name varchar(255),
      planet_name varchar(255),
      terrain varchar(255),
      climate varchar(255),
      gravity varchar(255)
    );
    """
    population_query = """
    INSERT INTO homeworlds
    SELECT
      p.name AS name,
      pl.name AS planet_name,
      pl.terrain AS terrain,
      pl.climate AS climate,
      pl.gravity AS gravity
    FROM people p
    LEFT JOIN planets pl ON p.homeworld = pl.url;
    """

    cursor = connection.cursor()
    cursor.execute(creation_query)
    cursor.execute(population_query)


def pandas_join_into_table(db_engine):
    # TODO achieve the same result as `join_into_table`, but by first
    # reading the entire tables into pandas DataFrames, then
    # joining them using pandas, before inserting them into the "homeworlds" table
    ...


def main():
    # TODO with-statement and `join_into_table` with `pandas_join_into_table`
    # as indicated by the commented out lines further down
    with db.connect() as connection:
        join_into_table(connection)
        connection.commit()

    # NOTE that with the higher level `engine` and pandas `.read_sql_table`/`.to_sql`-syntax
    # you don't need to use `with db.connect() ...`
    # db_engine = db.get_engine()
    # pandas_join_into_table(db_engine)


if __name__ == "__main__":
    main()
