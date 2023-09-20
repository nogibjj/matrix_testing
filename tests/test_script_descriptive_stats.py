"We will use pytest to test our functions from src/script_descriptive_stats.py:"
import sys
sys.path.append("/workspaces/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject")
sys.path.append("/workspaces/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/src")
from src.script_descriptive_stats import run_descriptive_stats
import pandas as pd


def test_descriptive_stats():
    "Test the descriptive stats function"
    data = pd.read_csv("data/iris_data.csv")
    target_column = "sepal_length"

    results = run_descriptive_stats(data, target_column)

    assert 'Target Column' in results
    assert '25th Quantile' in results
    assert 'Mean' in results
    assert 'Median' in results
    assert 'Standard Deviation' in results
