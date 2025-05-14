import sys
import os
import unittest
import pandas as pd
from etl.transform.transform import (
    drop_unnecessary_columns,
    preprocess_avg_speed_column,
    convert_elevation,
    clean_large_nums)

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))


class TestTransformFunctions(unittest.TestCase):
    def setUp(self):
        #  Create sample DF
        self.sample_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
            "Title": ["Test Run 1", "Test Cardio 1"],
            "Distance": [5.0, 2.5],
            "Calories": ["3,000", 150],
            "Total Time": ["00:30:00", "00:15:00"],
            "Avg HR": [120, 110],
            "Max HR": [150, 140],
            "Avg Speed": ["5:20", "--"],
            "Total Ascent": [50, 30],
            "Total Descent": [50, 30],
            "Steps": [5000, 3000],
            "Best Lap Time": ["00:01:00", "00:00:50"],
            "Number of Laps": [4, 3],
            "Moving Time": ["00:29:00", "00:14:00"],
            "Elapsed Time": ["00:30:00", "00:15:00"],
            "Min Elevation": ["2,500", "--"],
            "Max Elevation": ["1,200", "--"],
            "Favorite": [False, True],
            "Aerobic TE": [3.0, 2.5],
            "Avg Bike Cadence": [80, 85],
            "Max Bike Cadence": [100, 95],
            "Max Speed": [6.0, 5.5],
            "Avg Stride Length": [1.2, 1.1],
            "Avg GAP": [5.0, 4.8],
            "Normalized Power® (NP®)": [200, 180],
            "Training Stress Score®": [50, 40],
            "Avg Power": [150, 140],
            "Max Power": [300, 250],
            "Total Strokes": [None, None],
            "Avg. Swolf": [None, None],
            "Avg Stroke Rate": [None, None],
            "Decompression": ["No", "No"],
            "Total Runs": [None, None],
            "Longest Run": [None, None],
            "Active Time": ["00:30:00", "00:15:00"],
            "Total Run Distance": [5.0, 2.5],
            "Avg Run Speed": [5.0, 4.5],
            "Max Speed.1": ["20.0", "--"]
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
                "Avg Speed": ["5:20", "--"],
                "Total Ascent": [50, 30],
                "Total Descent": [50, 30],
                "Steps": [5000, 3000],
                "Best Lap Time": ["00:01:00", "00:00:50"],
                "Number of Laps": [4, 3],
                "Moving Time": ["00:29:00", "00:14:00"],
                "Elapsed Time": ["00:30:00", "00:15:00"],
                "Min Elevation": ["2,500", "--"],
                "Max Elevation": ["1,200", "--"]
        })

        result_df = drop_unnecessary_columns(self.sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_preprocess_avg_speed_column(self):

        expected_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
            "Title": ["Test Run 1", "Test Cardio 1"],
            "Distance": [5.0, 2.5],
            "Calories": ["3,000", 150],
            "Total Time": ["00:30:00", "00:15:00"],
            "Avg HR": [120, 110],
            "Max HR": [150, 140],
            "Avg Speed": ["00:05:20", None],
            "Total Ascent": [50, 30],
            "Total Descent": [50, 30],
            "Steps": [5000, 3000],
            "Best Lap Time": ["00:01:00", "00:00:50"],
            "Number of Laps": [4, 3],
            "Moving Time": ["00:29:00", "00:14:00"],
            "Elapsed Time": ["00:30:00", "00:15:00"],
            "Min Elevation": ["2,500", "--"],
            "Max Elevation": ["1,200", "--"],
            #  Below are the dropped columns to satisfy the test
            "Favorite": [False, True],
            "Aerobic TE": [3.0, 2.5],
            "Avg Bike Cadence": [80, 85],
            "Max Bike Cadence": [100, 95],
            "Max Speed": [6.0, 5.5],
            "Avg Stride Length": [1.2, 1.1],
            "Avg GAP": [5.0, 4.8],
            "Normalized Power® (NP®)": [200, 180],
            "Training Stress Score®": [50, 40],
            "Avg Power": [150, 140],
            "Max Power": [300, 250],
            "Total Strokes": [None, None],
            "Avg. Swolf": [None, None],
            "Avg Stroke Rate": [None, None],
            "Decompression": ["No", "No"],
            "Total Runs": [None, None],
            "Longest Run": [None, None],
            "Active Time": ["00:30:00", "00:15:00"],
            "Total Run Distance": [5.0, 2.5],
            "Avg Run Speed": [5.0, 4.5],
            "Max Speed.1": ["20.0", "--"]
        })

        result_df = preprocess_avg_speed_column(self.sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_convert_elevation(self):
        expected_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
            "Title": ["Test Run 1", "Test Cardio 1"],
            "Distance": [5.0, 2.5],
            "Calories": ["3,000", 150],
            "Total Time": ["00:30:00", "00:15:00"],
            "Avg HR": [120, 110],
            "Max HR": [150, 140],
            "Avg Speed": ["5:20", "--"],
            "Total Ascent": [50, 30],
            "Total Descent": [50, 30],
            "Steps": [5000, 3000],
            "Best Lap Time": ["00:01:00", "00:00:50"],
            "Number of Laps": [4, 3],
            "Moving Time": ["00:29:00", "00:14:00"],
            "Elapsed Time": ["00:30:00", "00:15:00"],
            "Min Elevation": ["2,500", "85"],
            "Max Elevation": ["1,200", "85"],
            #  Below are the dropped columns to satisfy the test
            "Favorite": [False, True],
            "Aerobic TE": [3.0, 2.5],
            "Avg Bike Cadence": [80, 85],
            "Max Bike Cadence": [100, 95],
            "Max Speed": [6.0, 5.5],
            "Avg Stride Length": [1.2, 1.1],
            "Avg GAP": [5.0, 4.8],
            "Normalized Power® (NP®)": [200, 180],
            "Training Stress Score®": [50, 40],
            "Avg Power": [150, 140],
            "Max Power": [300, 250],
            "Total Strokes": [None, None],
            "Avg. Swolf": [None, None],
            "Avg Stroke Rate": [None, None],
            "Decompression": ["No", "No"],
            "Total Runs": [None, None],
            "Longest Run": [None, None],
            "Active Time": ["00:30:00", "00:15:00"],
            "Total Run Distance": [5.0, 2.5],
            "Avg Run Speed": [5.0, 4.5],
            "Max Speed.1": ["20.0", "--"]
        })

        result_df = convert_elevation(self.sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)  

    def test_clean_large_numbers(self):

        expected_df = pd.DataFrame({
            "Activity Type": ["Running", "Cardio"],
            "Date": ["2025-05-01 16:10:50", "2025-05-02 10:00:00"],
            "Title": ["Test Run 1", "Test Cardio 1"],
            "Distance": [5.0, 2.5],
            "Calories": ["3000", 150],
            "Total Time": ["00:30:00", "00:15:00"],
            "Avg HR": [120, 110],
            "Max HR": [150, 140],
            "Avg Speed": ["5:20", "--"],
            "Total Ascent": [50, 30],
            "Total Descent": [50, 30],
            "Steps": [5000, 3000],
            "Best Lap Time": ["00:01:00", "00:00:50"],
            "Number of Laps": [4, 3],
            "Moving Time": ["00:29:00", "00:14:00"],
            "Elapsed Time": ["00:30:00", "00:15:00"],
            "Min Elevation": ["2500", "--"],
            "Max Elevation": ["1200", "--"],
            #  Below are the dropped columns to satisfy the test
            "Favorite": [False, True],
            "Aerobic TE": [3.0, 2.5],
            "Avg Bike Cadence": [80, 85],
            "Max Bike Cadence": [100, 95],
            "Max Speed": [6.0, 5.5],
            "Avg Stride Length": [1.2, 1.1],
            "Avg GAP": [5.0, 4.8],
            "Normalized Power® (NP®)": [200, 180],
            "Training Stress Score®": [50, 40],
            "Avg Power": [150, 140],
            "Max Power": [300, 250],
            "Total Strokes": [None, None],
            "Avg. Swolf": [None, None],
            "Avg Stroke Rate": [None, None],
            "Decompression": ["No", "No"],
            "Total Runs": [None, None],
            "Longest Run": [None, None],
            "Active Time": ["00:30:00", "00:15:00"],
            "Total Run Distance": [5.0, 2.5],
            "Avg Run Speed": [5.0, 4.5],
            "Max Speed.1": ["20.0", "--"]
        })

        result_df = clean_large_nums(self.sample_df)

        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == "__main__":
    unittest.main()
