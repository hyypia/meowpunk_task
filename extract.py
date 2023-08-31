from datetime import datetime

import pandas as pd

from db import read_from_db, write_to_db, create_db
from db_queries import select_query, insert_to_db


def extract_data_by_date(file_path: str, target_date: datetime.date) -> pd.DataFrame:
    filtered_data = []
    df = pd.read_csv(file_path)

    for i in range(len(df)):
        date = pd.Timestamp(df["timestamp"][i], unit="s").date()
        if date == target_date:
            df["prev_day"] = pd.Timestamp(df["timestamp"][i], unit="s") - pd.DateOffset(
                days=1
            )
            filtered_data.append((df.iloc[i]))

    cols = [
        "timestamp",
        "player_id" if "client" in file_path else "event_id",
        "error_id",
        "description",
        "prev_day",
    ]
    data = pd.DataFrame(filtered_data, columns=cols)
    return data


def exclude_cheaters(db_path: str, df: pd.DataFrame) -> pd.DataFrame:
    table = "cheaters"
    for_exclude = []

    cheaters_df = read_from_db(db_path, select_query(table))

    for i in range(len(df)):
        if df["player_id"][i] in cheaters_df["player_id"].values:
            ban_date = pd.Timestamp(cheaters_df["ban_time"][i], unit="s")
            if df["prev_day_y"][i] <= ban_date:
                for_exclude.append((df.iloc[i]))

    cols = ["player_id"]
    exclude = pd.DataFrame(for_exclude, columns=cols)

    filtered_df = pd.merge(df, exclude, on="player_id", how="outer")

    return filtered_df


def extract(
    client_file_path: str,
    server_file_path: str,
    cheaters_db_path: str,
    target_date: datetime.date,
):
    client_df = extract_data_by_date(client_file_path, target_date)
    server_df = extract_data_by_date(server_file_path, target_date)

    merged_data = pd.merge(client_df, server_df, on="error_id")

    filtered_df = exclude_cheaters(cheaters_db_path, merged_data)

    return filtered_df


def load(db_path: str, data: pd.DataFrame) -> None:
    create_db(db_path)

    for i in range(len(data)):
        record = (
            int(data["timestamp_y"][i]),
            int(data["player_id"][i]),
            int(data["event_id"][i]),
            data["error_id"][i],
            data["description_y"][i],
            data["description_x"][i],
        )
        write_to_db(db_path, insert_to_db, record)
