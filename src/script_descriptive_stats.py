"""Script to run descriptive statistics on the iris dataset,
using common fucntions from lib.py"""
import sys
import pandas as pd
try:
    import lib
except ModuleNotFoundError:
    sys.path.insert(1, './src')
    import lib


def run_descriptive_stats(data_: pd.DataFrame, target_column: str) -> dict:
    "Runs descriptive statistics on the passed dataset"

    res = {
        'Target Column': target_column,
        '25th Quantile': round(lib.return_25th_quantile(data_, target_column), 2),
        'Mean': round(lib.return_mean(data_, target_column), 2),
        'Median': round(lib.return_median(data_, target_column), 2),
        'Standard Deviation': round(lib.return_std_dev(data_, target_column), 2)
    }

    return res

def run_visualizations(data_: pd.DataFrame, outcome_var: str, target_var: str,
                       inteaction_term: str) -> None:
    "Runs visualizations on the passed dataset"
    lib.plot_hist(data_, target_var, jupyter=False)
    lib.visualize_dataset(data_, outcome_var, target_var, inteaction_term, 
                          jupyter=False)

if __name__ == '__main__':
    data = pd.read_csv("data/iris_data.csv")
    TARGET_COLUMN = "sepal_length"

    results = run_descriptive_stats(data, TARGET_COLUMN)
    for key, value in results.items():
        print(f'{key}: {value}')

    run_visualizations(data, "petal_width", TARGET_COLUMN, "species")
