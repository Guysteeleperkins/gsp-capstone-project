import pandas as pd


def join_dataframes(df1, df2, df3):
    """
    Joins three DataFrames on the 'Date' column using the nearest date.
    Assumes all DataFrames have a 'Date' column. merge_asof is used to merge
    two DataFrames by the "nearest key" rather than exact matches, perfect
    for merging these DataFrames as RHR and stress are recorded every 7 days
    """
    # Sort by 'Date' to satisfy merge_asof requirements
    df1 = df1.sort_values(by='Date')
    df2 = df2.sort_values(by='Date')
    df3 = df3.sort_values(by='Date')

    # Joining resting heart rate to activities
    df_combined = pd.merge_asof(df1, df2, on='Date', direction='backward')

    # joining df_combined with stress
    df_combined = pd.merge_asof(df_combined, df3, on='Date',
                                direction='backward')

    df_combined.set_index('Date', inplace=True)

    return df_combined
