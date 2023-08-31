import os
from datetime import datetime
from pathlib import Path

from memory_profiler import profile

from extract import extract, load


def get_date() -> datetime.date:
    input_date = input("Insert date in YYYY-MM-DD format please: ")
    date = datetime.strptime(input_date, "%Y-%m-%d").date()
    return date


@profile
def main(
    client_file_path: str, server_file_path: str, cheaters_db_path: str, db_path: str
):
    target_date = get_date()

    filtered_df = extract(
        client_file_path, server_file_path, cheaters_db_path, target_date
    )

    load(db_path, filtered_df)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    CLIENT_CSV = os.path.join(BASE_DIR, "data/client.csv")
    SERVER_CSV = os.path.join(BASE_DIR, "data/server.csv")
    CHEATERS_DB = os.path.join(BASE_DIR, "data/cheaters.db")
    DB = os.path.join(BASE_DIR, "task.db")

    main(CLIENT_CSV, SERVER_CSV, CHEATERS_DB, DB)
