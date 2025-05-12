import os
import sys
from config.env_config import setup_env
from etl.extract.extract import extract_and_load_data
from etl.transform.transform import clean_and_transform_data


def main():
    run_env_setup()

    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )

    df = extract_and_load_data("./data/raw/ActivitiesGarmin.csv")
    df = clean_and_transform_data(df)

    return df


def run_env_setup():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
