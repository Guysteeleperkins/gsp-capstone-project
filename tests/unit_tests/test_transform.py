import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

import unittest
import pandas as pd
from etl.transform.transform import drop_unnecessary_columns
    # preprocess_avg_speed_column,
    # convert_to_nulls,
    # create_booleans,
    # convert_elevation,
    # convert_steps,
    # clean_large_nums,
    # convert_ascent_descent,
    # convert_data_type,
    # clean_total_asc_des,
    # fill_step_nones,
    # remove_columns_with_tt_below_ten_mins


class TestTransformFunctions(unittest.TestCase):
    def setUp(self):
        #  Create sample DF
        self.sample_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
            "Favorite": [False, True],
            "Title": ["Test Run 1", "Test Cardio 1"],
            "Distance": [5.0, 2.5],
            "Calories": ["3,000", 150],
            "Total Time": ["00:30:00", "00:15:00"],
            "Avg HR": [120, 110],
            "Max HR": [150, 140],
            "Aerobic TE": [3.0, 2.5],
            "Avg Bike Cadence": [80, 85],
            "Max Bike Cadence": [100, 95],
            "Avg Speed": [5.0, "--"],
            "Max Speed": [6.0, 5.5],
            "Total Ascent": [50, 30],
            "Total Descent": [50, 30],
            "Avg Stride Length": [1.2, 1.1],
            "Avg GAP": [5.0, 4.8],
            "Normalized Power® (NP®)": [200, 180],
            "Training Stress Score®": [50, 40],
            "Avg Power": [150, 140],
            "Max Power": [300, 250],
            "Total Strokes": [None, None],
            "Avg. Swolf": [None, None],
            "Avg Stroke Rate": [None, None],
            "Steps": [5000, 3000],
            "Decompression": ["No", "No"],
            "Best Lap Time": ["00:01:00", "00:00:50"],
            "Number of Laps": [4, 3],
            "Total Runs": [None, None],
            "Longest Run": [None, None],
            "Active Time": ["00:30:00", "00:15:00"],
            "Total Run Distance": [5.0, 2.5],
            "Avg Run Speed": [5.0, 4.5],
            "Moving Time": ["00:29:00", "00:14:00"],
            "Elapsed Time": ["00:30:00", "00:15:00"],
            "Max Speed.1": ["20.0", "--"],
            "Min Elevation": [10, 5],
            "Max Elevation": [50, 30]
        })

    def test_drop_unnecessary_columns(self):
        # Expected output after dropping
        expected_df = pd.DataFrame({
                "Activity Type": ["Running", "Cardio"],
                "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
                "Title": ["Test Run 1", "Test Cardio 1"],
                "Distance": [5.0, 2.5],
                "Calories": ["3,000", 150],
                "Total Time": ["00:30:00", "00:15:00"],
                "Avg HR": [120, 110],
                "Max HR": [150, 140],
                "Avg Speed": [5.0, "--"],
                "Total Ascent": [50, 30],
                "Total Descent": [50, 30],
                "Steps": [5000, 3000],
                "Best Lap Time": ["00:01:00", "00:00:50"],
                "Number of Laps": [4, 3],
                "Moving Time": ["00:29:00", "00:14:00"],
                "Elapsed Time": ["00:30:00", "00:15:00"],
                "Min Elevation": [10, 5],
                "Max Elevation": [50, 30]
        })

        result_df = drop_unnecessary_columns(self.sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == "__main__":
    unittest.main()
