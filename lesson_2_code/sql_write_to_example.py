import pandas as pd

import db


if __name__ == '__main__':
    new_example_rows = pd.DataFrame({'my_1st_col': [7, 8], 'my_2nd_col': [9, 10]})

    db_engine = db.get_engine()
    new_example_rows.to_sql('example', db_engine, if_exists='append', index=False)
