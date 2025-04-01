import random
import os
from utils import set_seed, save_dicts_to_csv

def simulate_occupancy(num_bins, num_balls, num_trials):
    results = []
    for _ in range(num_trials):
        bins = [0] * num_bins
        for _ in range(num_balls):
            bin_index = random.randint(0, num_bins - 1)
            bins[bin_index] += 1

        empty_bins = sum(1 for count in bins if count == 0)
        collisions = sum(1 for count in bins if count > 1)
        max_load = max(bins)

        results.append({
            "empty_bins": empty_bins,
            "collisions": collisions,
            "max_load": max_load
        })
    return results

if __name__ == "__main__":
    set_seed(42)
    results = simulate_occupancy(num_bins=100, num_balls=200, num_trials=1000)
    os.makedirs("../outputs", exist_ok=True)
    save_dicts_to_csv(results, "../outputs/simulation_results.csv")
