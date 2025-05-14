import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

import unittest
import pandas as pd
from etl.transform.transform import (
    create_booleans,
    convert_elevation,
    convert_steps,
    convert_ascent_descent,
    convert_data_type,
    clean_total_asc_des,
    fill_step_nones,
    remove_columns_with_tt_below_ten_mins
)