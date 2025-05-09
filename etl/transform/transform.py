import pandas as pd


def clean_and_transform_data(df):
    """Clean the loaded data from the ActivitiesGarmin dataset"""
    df = drop_unnecessary_columns(df)
    df = convert_to_nulls(df)
    df = create_booleans(df)
    df = convert_elevation(df)
    df = convert_steps(df)
    df = convert_ascent_descent(df)
    df = convert_data_type(df)
    df = remove_columns_with_tt_below_ten_mins(df)
    to_csv(df)
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
    df["Max Speed"] = df["Max Speed"].apply(parse_avg_speed)
    return df


def convert_elevation(df):
    """Converting null values represented as '--' to 85m as all recorded
    with out min or max will be at my gym at 85m"""
    def parse_elevation(value):
        if isinstance(value, str) and "-" not in value:
            value = value
        else:
            value = "85"
        return value

    df["Min Elevation"] = df["Min Elevation"].apply(parse_elevation)
    df["Max Elevation"] = df["Max Elevation"].apply(parse_elevation)
    return df


def convert_steps(df):
    def parse_steps(value):
        if isinstance(value, str) and "-" not in value:
            value = value
        else:
            value = "0"
        return value

    df["Steps"] = df["Steps"].apply(parse_steps)
    return df


def convert_ascent_descent(df):
    def parse_ascent_descent(value):
        if isinstance(value, str) and "-" not in value:
            value = value
        else:
            value = "0"
        return value

    df["Total Ascent"] = df["Total Ascent"].apply(parse_ascent_descent)
    df["Total Descent"] = df["Total Descent"].apply(parse_ascent_descent)

    return df


def create_booleans(df):
    """Creating new columns to keep track of filled na's"""
    df["Avg Speed Removed"] = df["Avg Speed"].isna()

    return df


def convert_data_type(df):
    df["Avg Speed"] = pd.to_timedelta(df["Avg Speed"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df["Total Time"] = pd.to_timedelta(df["Total Time"], errors='coerce')
    df["Best Lap Time"] = pd.to_timedelta(df["Best Lap Time"], errors='coerce')
    df["Moving Time"] = pd.to_timedelta(df["Moving Time"], errors='coerce')

    return df


def remove_columns_with_tt_below_ten_mins(df):
    """A few recorded activity's are recording errors or
    accidental and would skew data - removing rows that have a
    total time of less than 10 minutes"""
    df = df[df["Total Time"] >= pd.to_timedelta("00:10:00")]

    return df


def to_csv(df):
    df.to_csv('./data/processed/CleanedActivitiesGarmin.csv')
