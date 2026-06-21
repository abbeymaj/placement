# Importing packages
import os
import pytest
from src.utils import read_sql_data
from src.monitoring.detect_drift import DetectDataDrift

# Verifying that the data can be read from the data database
def test_read_sql_data(table='data'):
    df = read_sql_data(table)
    assert df is not None
    assert df.shape[0] > 0
    assert df.shape[1] > 1

# Verifying that the data can be read from the databases and merged correctly
def test_read_data_from_db():
    drift = DetectDataDrift()
    db_data = drift.read_data_from_db()
    assert db_data is not None
    assert db_data.shape[0] > 0

# Verifying that the detect data drift function runs as expected
def test_detect_data_drift():
    drift = DetectDataDrift()
    drift.detect_data_drift(save_report=False)
    