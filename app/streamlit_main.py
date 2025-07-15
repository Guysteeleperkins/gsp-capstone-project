import sys
import os
import streamlit as st
from metrics_visuals import (display_metrics,
                                 display_visualizations,
                                 display_dataframe)
from read_csv import read_cleaned_csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main():
    """Main function to run the Streamlit App"""
    st.set_page_config(
        page_title="GSP Garmin Data",
        page_icon="🏃🏼‍♂️",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # Set the title of the page
    st.title("GSP Garmin Dataset Explorer")

    # Set dataframe
    df = read_cleaned_csv("./data/processed/CleanedActivitiesGarmin.csv")

    # Display Metrics
    display_metrics(df)

    display_visualizations(df)

    display_dataframe(df)


if __name__ == "__main__":
    main()
