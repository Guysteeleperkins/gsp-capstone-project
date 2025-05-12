import pandas as pd


def weekly_activities(df):
    weekly_df = df[['Date', 'Activity']]
    weekly_df["Date"] = pd.to_datetime(df['Date'])
    weekly_df['Week'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)
    print(weekly_df)
    # return df.groupby('Week').size()
