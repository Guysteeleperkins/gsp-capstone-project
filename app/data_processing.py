import pandas as pd


def weekly_activities(df):
    weekly_df = df[['Activity Type', 'Date']].copy()
    weekly_df["Date"] = pd.to_datetime(weekly_df['Date'], errors='coerce')
    weekly_df['Week'] = weekly_df['Date'].dt.to_period('W').apply(
        lambda r: r.start_time)
    return weekly_df.groupby('Week').size().reset_index(name='Activity Count')
