import pandas as pd


def clean_and_transform_data(df):
    """Clean the loaded data from the ActivitiesGarmin dataset"""
    df = drop_unnecessary_columns(df)
    df = convert_to_nulls(df)
    # df = convert_to_na(df)
    # df = create_booleans(df)
    # df = clean_numerical_columns(df)
    return df


def drop_unnecessary_columns(df):
    """Drop any unnecessary columns and duplicates"""
    df.drop(columns=["Favorite",
                     "Avg Bike Cadence",
                     "Max Bike Cadence",
                     "Total Strokes",
                     "Avg. Swolf",
                     "Avg Stroke Rate",
                     "Decompression",
                     "Normalized Power® (NP®)",
                     "Total Runs",
                     "Longest Run",
                     "Active Time",
                     "Total Run Distance",
                     "Avg Run Speed",
                     "Max Speed",
                     "Avg Power",
                     "Max Power",
                     "Aerobic TE",
                     "Avg Stride Length",
                     "Avg GAP",
                     "Max Speed.1",
                     "Training Stress Score®"],
            inplace=True)
    df.drop_duplicates(inplace=True)
    return df


def convert_to_nulls(df):
    """As some "activities" involve other time formats and are inaccurate due
    to the type of session e.g a lot of "Cardio" sessions are resistance
    so an Avg speed would not make sense -> these are converted to None values"""
    def parse_avg_speed(value):
        if isinstance(value, str) and ":" in value:
            value = value
        else:
            value = None
        return value

    df["Avg Speed"] = df["Avg Speed"].apply(parse_avg_speed)

    return df["Avg Speed"]


# def create_booleans(df):
#     """Creating new columns to keep track of filled na's"""
#     df["Avg Speed Inputted"] = df["Avg Speed"].isna()


# def clean_numerical_columns(df):
#     df["Total Ascent"] = df["Total Ascent"].fillna(0)
#     df["Total Descent"] = df["Total Ascent"].fillna(0)
#     cardio_mean_speed = df.loc[df["Activity Type"] == 'Cardio', 'Avg Speed'].mean()
#     df["Avg Speed"] = df["Avg Speed"].fillna(cardio_mean_speed)
