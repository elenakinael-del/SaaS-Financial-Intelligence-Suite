import runpy
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_dashboard_mart_has_one_row_per_month_and_valid_arr():
    runpy.run_path(str(ROOT / "2_Data_Engine_Layer" / "3_SaaS_Dashboard_Engine.py"))
    frame = pd.read_csv(ROOT / "2_Data_Engine_Layer" / "SaaS_Executive_Dashboard_Metrics.csv")
    assert frame["Month"].is_unique
    assert np.isclose(frame["ARR"], frame["MRR"] * 12).all()
    assert (frame["Active_Customers"] > 0).all()
