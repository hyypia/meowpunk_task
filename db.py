import sqlite3
from sqlite3 import Error

import pandas as pd

from db_queries import create_table


def create_db(db: str) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()
    try:
        cur.execute(create_table)
    except Error as e:
        print(f"DB execute ERROR: {e}")
    finally:
        print("DB inited successfilly")


def read_from_db(db: str, sql: str) -> pd.DataFrame:
    con = sqlite3.connect(db)
    data = pd.read_sql_query(sql, con)
    con.close()

    return data


def write_to_db(db: str, sql: str, params=None) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()
    if params is None:
        params = ()
    cur.execute(sql, params)
    con.commit()
    con.close()


if __name__ == "__main__":
    db = "task.db"
    create_db(db)
