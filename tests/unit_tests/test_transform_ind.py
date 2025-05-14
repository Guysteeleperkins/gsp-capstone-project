import sys
import os
import unittest
import pandas as pd
from etl.transform.transform import (
    create_booleans,
    convert_elevation,
    convert_steps,
    convert_ascent_descent,
    clean_total_asc_des,
    fill_step_nones,
    remove_columns_with_tt_below_ten_mins
)

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))


class TestTransformFunctionsOne(unittest.TestCase):
    def test_create_booleans(self):
        sample_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Avg Speed": [None, "5:20"]
        })

        expected_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Avg Speed": [None, "5:20"],
            "Avg Speed Removed": [True, False]
        })

        result_df = create_booleans(sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_convert_elevation(self):
        sample_df = pd.DataFrame({
            "Min Elevation": ["200", "--"],
            "Max Elevation": ["--", 120]
        })

        expected_df = pd.DataFrame({
            "Min Elevation": ["200", "85"],
            "Max Elevation": ["85", 120]
        })

        result_df = convert_elevation(sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_convert_steps(self):
        sample_df = pd.DataFrame({
            "Steps": ["200", "--", 14]
        })

        expected_df = pd.DataFrame({
            "Steps": ["200", "0", 14]
        })

        result_df = convert_steps(sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_convert_ascent_descent(self):
        sample_df = pd.DataFrame({
            "Total Ascent": ["200", "--", 14],
            "Total Descent": [1560, "--", "500"]
        })

        expected_df = pd.DataFrame({
            "Total Ascent": ["200", "0", 14],
            "Total Descent": [1560, "0", "500"]
        })

        result_df = convert_ascent_descent(sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_clean_total_asc_des(self):
        sample_df = pd.DataFrame({
            "Total Ascent": [200, None],
            "Total Descent": [None, None],
            "Max Elevation": [200, 500],
            "Min Elevation": [50, 150]
        })

        expected_df = pd.DataFrame({
            "Total Ascent": [200, 350],
            "Total Descent": [200, 350],
            "Max Elevation": [200, 500],
            "Min Elevation": [50, 150]
        })

        result_df = clean_total_asc_des(sample_df)

        result_df["Total Ascent"] = result_df["Total Ascent"].astype("int64")
        result_df["Total Descent"] = result_df["Total Descent"].astype("int64")

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_fill_step_nones(self):
        sample_df = pd.DataFrame({
            "Steps": [200, None, 14]
        })

        expected_df = pd.DataFrame({
            "Steps": [200, 107, 14]
        })

        result_df = fill_step_nones(sample_df)

        result_df["Steps"] = result_df["Steps"].astype("int64")

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_remove_columns_with_tt_below_ten_mins(self):
        sample_df = pd.DataFrame({
            "Total Time": ["00:30:25", "01:20:14", "00:04:14"]
        })

        expected_df = pd.DataFrame({
            "Total Time": ["00:30:25", "01:20:14"]
        })

        expected_df["Total Time"] = pd.to_timedelta(expected_df["Total Time"],
                                                    errors='coerce')
        sample_df["Total Time"] = pd.to_timedelta(sample_df["Total Time"],
                                                  errors='coerce')

        result_df = remove_columns_with_tt_below_ten_mins(sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)


# Run all tests
if __name__ == "__main__":
    unittest.main()
