import pandas as pd

import db


if __name__ == '__main__':
    db_engine = db.get_engine()
    df = pd.read_sql_table('example', db_engine)

    print()
    print("table content:")
    print(df)
    print()
    print("table content summary description:")
    print(df.describe())
