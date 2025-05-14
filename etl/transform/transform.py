import pandas as pd


def clean_and_transform_data(df):
    """Clean the loaded data from the ActivitiesGarmin dataset"""
    df = drop_unnecessary_columns(df)
    df = preprocess_avg_speed_column(df)
    df = convert_to_nulls(df)
    df = create_booleans(df)
    df = convert_elevation(df)
    df = convert_steps(df)
    df = clean_large_nums(df)
    df = convert_ascent_descent(df)
    df = convert_data_type(df)
    df = clean_total_asc_des(df)
    df = fill_step_nones(df)
    df = remove_columns_with_tt_below_ten_mins(df)
    return df


def drop_unnecessary_columns(df):
    """Drop any unnecessary columns and duplicates"""
    df.drop(columns=["Favorite",
                     "Avg Bike Cadence",
                     "Max Speed",  # Potentially use this!
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


def preprocess_avg_speed_column(df):
    """Preprocess the Avg Speed column to make it compatible
    with pd.to_timedelta."""
    def format_time(value):
        if isinstance(value, str) and ":" in value:
            # Add "00:" if the value is in "MM:SS" format
            parts = value.split(":")
            if len(parts) == 2:  # MM:SS
                minutes = parts[0].zfill(2)  # Ensure minutes are 2 digits
                seconds = parts[1].zfill(2)  # Ensure seconds are 2 digits
                return f"00:{minutes}:{seconds}"
            elif len(parts) == 3:  # HH:MM:SS
                hours = parts[0].zfill(2)    # Ensure hours are 2 digits
                minutes = parts[1].zfill(2)  # Ensure minutes are 2 digits
                seconds = parts[2].zfill(2)  # Ensure seconds are 2 digits
                return f"{hours}:{minutes}:{seconds}"
        return None  # For invalid or missing values

    df["Avg Speed"] = df["Avg Speed"].apply(format_time)

    return df


def convert_to_nulls(df):
    """As some "activities" involve other time formats and are inaccurate due
    to the type of session e.g a lot of "Cardio" sessions are resistance
    so an Avg speed would not make sense -> these are converted to None
    values"""
    def parse_avg_speed(value):
        if isinstance(value, str) and ":" in value:
            return value
        else:
            return None

    df["Avg Speed"] = df["Avg Speed"].apply(parse_avg_speed)
    # df["Max Speed"] = df["Max Speed"].apply(parse_avg_speed)
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


def clean_total_asc_des(df):
    """Calculating total ascent and descent using elevation"""
    def parse_acs_des(value, max_elevation, min_elevation):
        if value is None or pd.isna(value):
            return abs(max_elevation - min_elevation)
        return value

    df["Total Ascent"] = df.apply(
        lambda row: parse_acs_des(row["Total Ascent"],
                                  row["Max Elevation"],
                                  row["Min Elevation"]),
        axis=1
        )

    df["Total Descent"] = df.apply(
        lambda row: parse_acs_des(row["Total Ascent"],
                                  row["Max Elevation"],
                                  row["Min Elevation"]),
        axis=1
        )

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


def clean_large_nums(df):
    def parse_large_nums(value):
        if isinstance(value, str) and "," not in value:
            return value
        elif isinstance(value, int):
            return value
        else:
            values = value.split(',')
            value = values[0] + values[1]
            return value

    df["Calories"] = df["Calories"].apply(parse_large_nums)
    df["Max Elevation"] = df["Max Elevation"].apply(parse_large_nums)
    df["Min Elevation"] = df["Min Elevation"].apply(parse_large_nums)
    return df


def fill_step_nones(df):
    """Calculate average steps and fill none values
    with this average"""

    if "Steps" in df.columns:
        # Calculate average steps
        average_steps = df["Steps"].mean().round(0)
        # Fill None values with average steps
        df["Steps"] = df["Steps"].fillna(average_steps)

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
    """Converts to correct and useful datatypes"""
    df["Avg Speed"] = pd.to_timedelta(df["Avg Speed"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df["Date"] = df["Date"].dt.date
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df["Total Time"] = pd.to_timedelta(df["Total Time"], errors='coerce')
    df["Best Lap Time"] = pd.to_timedelta(df["Best Lap Time"], errors='coerce')
    df["Moving Time"] = pd.to_timedelta(df["Moving Time"], errors='coerce')
    df["Calories"] = pd.to_numeric(df["Calories"], errors='coerce')
    df["Avg HR"] = pd.to_numeric(df["Avg HR"], errors='coerce')
    df["Max HR"] = pd.to_numeric(df["Max HR"], errors='coerce')
    df["Total Ascent"] = pd.to_numeric(df["Total Ascent"], errors='coerce')
    df["Total Descent"] = pd.to_numeric(df["Total Descent"], errors='coerce')
    df["Steps"] = pd.to_numeric(df["Steps"], errors='coerce')
    df["Elapsed Time"] = pd.to_timedelta(df["Elapsed Time"], errors='coerce')
    df["Min Elevation"] = pd.to_numeric(df["Min Elevation"], errors='coerce')
    df["Max Elevation"] = pd.to_numeric(df["Max Elevation"], errors='coerce')
    df["Distance"] = pd.to_numeric(df["Distance"], errors='coerce')

    return df


def remove_columns_with_tt_below_ten_mins(df):
    """A few recorded activity's are recording errors or
    accidental and would skew data - removing rows that have a
    total time of less than 10 minutes"""
    df = df[df["Total Time"] >= pd.to_timedelta("00:10:00")]

    return df
