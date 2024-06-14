"""
This module shows some examples on how to
create, populate, and interact with a SQLite
database using Python.
"""
import sqlite3


## -- Define and populate users table -- ##
def define_table_users(conn):
    """
    Create the users table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    cursor = conn.cursor()
    sql_statement = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE
    )
    """
    cursor.execute(sql_statement)


def insert_user_data(conn):
    """
    Insert some dummy data to the users table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    cursor = conn.cursor()
    users = [
        ("Alice", "alice@epr.org"),
        ("Bob", "bob@epr.org"),
        ("Eve", "eve@spectre.org"),
    ]

    cursor.executemany(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        users,
    )


## -- Define and populate items table -- ##
def define_table_items(conn):
    """
    Create the items table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    cursor = conn.cursor()
    sql_statement = """
    CREATE TABLE IF NOT EXISTS items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """
    cursor.execute(sql_statement)


def insert_item_data(conn):
    """
    Insert some dummy data to the order table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    cursor = conn.cursor()
    items = [
        ("Mystic Orb", 29.99),
        ("Enchanted Sword", 49.99),
        ("Potion of Healing", 9.99),
        ("Dragon Scale Armor", 199.99),
        ("Ancient Spellbook", 79.99),
    ]

    cursor.executemany(
        "INSERT INTO items (item_name, price) VALUES (?, ?)",
        items,
    )


## -- Define and populate orders table -- ##
def define_table_orders(conn):
    """
    Create the order table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    cursor = conn.cursor()
    sql_statement = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        order_date DATE NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(item_id) REFERENCES items(item_id)
    )
    """

    cursor.execute(sql_statement)


def insert_order_data(conn):
    """
    Insert some dummy data to the orders table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    None
        This function doesn't return anything.
    """
    orders = [
        (1, 1, 2, "2024-01-01"),
        (1, 2, 1, "2024-01-02"),
        (3, 2, 1, "2024-01-02"),
        (2, 3, 3, "2024-01-03"),
        (1, 4, 1, "2024-01-04"),
        (2, 5, 2, "2024-01-05"),
        (3, 4, 1, "2024-01-06"),
    ]

    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO orders (user_id, item_id, quantity, order_date) VALUES (?, ?, ?, ?)",
        orders,
    )


def fetch_users(conn):
    """
    Fetch all columns in the users table.

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.

    Returns
    -------
    list of tuple
        The user records in the database.
    """
    cursor = conn.cursor()

    sql = """
    SELECT
        *
    FROM users;
    """
    cursor.execute(sql)

    users = cursor.fetchall()
    return users


def execute_sql_query(conn, sql_query: str):
    """
    Execute sql_query.

    !!Note, this type of function is not generally
    recommended from a security point of view!!

    Parameters
    ----------
    conn : sqlite3.connection
        A connection to the SQLite database.
    sql_qery : str


    Returns
    -------
    list of tuple
        The records resulting from the query.
    """
    cursor = conn.cursor()
    cursor.execute(sql_query)

    output = cursor.fetchall()

    return output


def main():
    with sqlite3.connect("primer.db") as conn:
        define_table_users(conn)
        insert_user_data(conn)

        define_table_items(conn)
        insert_item_data(conn)

        define_table_orders(conn)
        insert_order_data(conn)

        print("####  users query  ####")
        users = fetch_users(conn)
        for user in users:
            print(user)

        print("\n####  joined query  ####")

        query = """
        SELECT
            u.username,
            u.email,
            i.item_name
        FROM users u
        JOIN orders o ON o.user_id = u.user_id
        JOIN items i ON i.item_id = o.item_id;
        """
        joined_output = execute_sql_query(conn, query)
        for output in joined_output:
            print(output)


if __name__ == "__main__":
    main()
