import pandas as pd

import db


def join_into_table(db_engine):

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

    joined_df = pd.read_sql_query(sql, db_engine)
    joined_df.to_sql("homeworlds", db_engine, if_exists="replace", index=False)


def pandas_join_into_table(db_engine):
    # TODO achieve the same result as `join_into_table`, but by first
    # reading the entire tables into pandas DataFrames, then
    # joining them using pandas, before inserting them into the "homeworlds" table
    ...


def main():
    db_engine = db.get_engine()
    join_into_table(db_engine)  # TODO replace with `pandas_join_into_table`


if __name__ == "__main__":
    main()
