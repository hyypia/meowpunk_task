create_table = """CREATE TABLE IF NOT EXISTS errors (
    timestamp DATETIME NOT NULL,
    player_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    error_id TEXT NOT NULL PRIMARY KEY,
    json_server TEXT,
    json_client TEXT
    )"""


def select_query(table: str, col="*") -> str:
    return f"SELECT {col} FROM {table}"


insert_to_db = """INSERT INTO
    errors (timestamp, player_id, event_id, error_id, json_server, json_client)
    VALUES (?, ?, ?, ?, ?, ?)"""
