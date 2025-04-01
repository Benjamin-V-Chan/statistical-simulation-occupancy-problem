import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_histogram(df, column, output_path):
    plt.figure()
    df[column].hist(bins=30)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv("../outputs/simulation_results.csv")
    os.makedirs("../outputs", exist_ok=True)

    for metric in ["empty_bins", "collisions", "max_load"]:
        plot_histogram(df, metric, f"../outputs/{metric}_hist.png")
