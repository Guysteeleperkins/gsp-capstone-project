import pandas as pd


def weekly_activities(df):
    """Function to create a DataFrame grouping number of activities per week"""
    weekly_df = df[['Activity Type', 'Date']].copy()
    weekly_df["Date"] = pd.to_datetime(weekly_df['Date'], errors='coerce')
    weekly_df['Week'] = weekly_df['Date'].dt.to_period('W').apply(
        lambda r: r.start_time)
    return weekly_df.groupby('Week').size().reset_index(name='Activity Count')


def weekly_avg_rhr(df):
    weekly_rhr_df = df[['Resting Heart Rate', 'Date']].copy()
    weekly_rhr_df["Date"] = pd.to_datetime(weekly_rhr_df['Date'],
                                           errors='coerce')
    weekly_rhr_df['Week'] = weekly_rhr_df['Date'].dt.to_period('W').apply(
        lambda r: r.start_time)
    return weekly_rhr_df.groupby('Week').mean()
