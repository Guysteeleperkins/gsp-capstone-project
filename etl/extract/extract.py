import pandas as pd


def extract_and_load_data(filepath):
    """Extract and Load the data from the ActivitesGarmin CSV Dataset"""
    return pd.read_csv(filepath)


def extract_rhr(filepath):
    """Extract and Load the data from the resting heart rate CSV Dataset"""
    return pd.read_csv(filepath)


def extract_stress(filepath):
    """Extract and Load the data from the stress CSV Dataset"""
    return pd.read_csv(filepath)
