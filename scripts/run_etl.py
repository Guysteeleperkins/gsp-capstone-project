import os
import sys
from config.env_config import setup_env
from etl.extract.extract import (extract_and_load_data,
                                 extract_rhr, extract_stress)
from etl.transform.transform import clean_and_transform_data
from etl.transform.join import join_dataframes
from etl.transform.transform_extras import transform_two_column_csvs


def main():
    run_env_setup()

    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )

    df_activities = extract_and_load_data("./data/raw/ActivitiesGarmin.csv")
    df_rhr = extract_rhr("./data/raw/Resting_heart_Rate.csv")
    df_stress = extract_stress("./data/raw/stress.csv")

    df_rhr = transform_two_column_csvs(df_rhr)
    df_stress = transform_two_column_csvs(df_stress)

    df_activities = clean_and_transform_data(df_activities)

    df = join_dataframes(df_activities, df_rhr, df_stress)

    df.to_csv("./data/processed/CleanedActivitiesGarmin.csv")

    return df


def run_env_setup():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
