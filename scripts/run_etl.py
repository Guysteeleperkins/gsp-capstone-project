import os
import subprocess
import sys
from config.env_config import setup_env
from etl.extract.extract import (
    extract_and_load_data, extract_rhr, extract_stress
    )
from etl.transform.transform import clean_and_transform_data
from etl.transform.join import join_dataframes
from etl.transform.transform_extras import transform_two_column_csvs


def main():
    run_env_setup()

    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )

    run_tests()

    data = run_extraction()

    df = run_transform(data)

    print("Converting DataFrame to cleaned CSV...")
    df.to_csv("./data/processed/CleanedActivitiesGarmin.csv")
    print("Transformed CSV creation successful.")
    return df


def run_env_setup():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


def run_tests():
    """Run unit tests before executing the pipeline.
    I did not create this code I used Copilot to help me
    create this function to run through tests smoothly"""
    print("Running tests...")
    result = subprocess.run(
        [sys.executable,
         "-m",
         "unittest",
         "discover",
         "-s",
         "tests/unit_tests",
         "-p",
         "test_*.py"
         ])
    if result.returncode != 0:
        print("Tests failed. Exiting pipeline.")
        sys.exit(1)
    print("All tests passed!")


def run_extraction():
    """Function to assign CSVs to DataFrames"""
    print("Reading CSV's and assigning to to DataFrames..")
    df_activities = extract_and_load_data("./data/raw/ActivitiesGarmin.csv")
    df_rhr = extract_rhr("./data/raw/Resting_heart_Rate.csv")
    df_stress = extract_stress("./data/raw/stress.csv")
    print("DataFrames created.")
    return df_activities, df_rhr, df_stress


def run_transform(data):
    """Function that cleans, transforms
    and joins the DataFrames for analysis"""
    print("Transforming data...")
    df_activities = clean_and_transform_data(data[0])
    df_rhr = transform_two_column_csvs(data[1])
    df_stress = transform_two_column_csvs(data[2])
    print("Data transformed")
    print("Joining DataFrames")
    df = join_dataframes(df_activities, df_rhr, df_stress)
    print("DataFrames joined.")

    return df


if __name__ == "__main__":
    main()
