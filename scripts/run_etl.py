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
    #  Run tests
    run_tests()
    #  Assign CSVs
    data = run_extraction()
    #  Transform CSVs
    df = run_transform(data)

    print("Converting DataFrame to cleaned CSV...")
    #  Convert DataFrame to cleaned CSV
    df.to_csv("./data/processed/CleanedActivitiesGarmin.csv")
    print("Transformed CSV creation successful.")

    #  Run Streamlit App
    run_streamlit_app()


def run_env_setup():
    print("Setting up environment...")
    try:
        setup_env(sys.argv)
        print("Environment setup complete.")
    except Exception as e:
        print(f"Error during environment setup: {e}")
        sys.exit(1)


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


def run_streamlit_app():
    """Launch Streamlit app"""
    """Copilot also helped me with this one too but I thought it was
    a cool feature"""
    print("Would you like to launch Streamlit App")
    choice = input("Enter your choice (y/n): ")

    if choice == "y":
        print("Launching Streamlit App...")
        try:
            # Set the PYTHONPATH environment variable
            env = os.environ.copy()
            env["PYTHONPATH"] = "."

            subprocess.run(["streamlit",
                            "run",
                            "app/streamlit_main.py"],
                           check=True,
                           env=env)
        except FileNotFoundError:
            print("""
                  Error: Streamlit is not installed.
                  Please install it using 'pip install streamlit'.""")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to launch Streamlit app. {e}")
            sys.exit(1)
    elif choice == "n":
        print("Streamlit launch aborted!")
    else:
        print("Invalid choice. Exiting")


if __name__ == "__main__":
    main()
