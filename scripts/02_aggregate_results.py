import pandas as pd
import os

def summarize_results(input_path, output_path):
    df = pd.read_csv(input_path)
    summary = df.describe().loc[["mean", "std", "min", "max"]]
    summary.to_csv(output_path)

if __name__ == "__main__":
    input_file = "../outputs/simulation_results.csv"
    output_file = "../outputs/summary_statistics.csv"
    summarize_results(input_file, output_file)
