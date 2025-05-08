import pandas as pd


def extract_and_load_data(filepath):
    """Extract and Load the data from the ActivitesGarmin CSV Dataset"""
    return pd.read_csv(filepath)
