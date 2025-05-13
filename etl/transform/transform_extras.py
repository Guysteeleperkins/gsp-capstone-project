import pandas as pd


def transform_two_column_csvs(df):
    name_date_column(df)
    convert_date(df)
    return df


def name_date_column(df):
    df.rename(columns={"Unnamed: 0": "Date"}, inplace=True)
    return df


def convert_date(df):
    start_year = 2024
    dates = []

    for date in df["Date"]:
        try:
            # parse the date with the current year
            parsed_date = pd.to_datetime(f"{date} {start_year}",
                                         errors='coerce')

            """if the parsed date is earlier than the 
            last year, increment the year"""
            if dates and parsed_date < dates[-1]:
                start_year += 1
                parsed_date = pd.to_datetime(f"{date} {start_year}",
                                             errors='coerce')

            dates.append(parsed_date)
        except Exception:
            dates.append(pd.NaT)

    df["Date"] = dates
    return df
