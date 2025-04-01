# statistical-simulation-occupancy-problem

## Project Overview

This project simulates the classical **occupancy problem** in probability theory and statistics. The problem explores how randomly assigning $n$ indistinguishable or distinguishable balls into $m$ distinguishable bins leads to various distribution patterns. This project empirically investigates metrics such as the number of **empty bins**, the number of **collisions** (bins with more than one ball), and the **maximum load** (maximum number of balls in any single bin).


## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_run_simulation.py         # Runs simulation and saves results
│   ├── 02_aggregate_results.py      # Summarizes output statistics
│   ├── 03_visualize_results.py      # Produces histograms for metrics
│   └── utils.py                     # Shared utility functions
├── outputs/
│   ├── simulation_results.csv       # Raw simulation output
│   ├── summary_statistics.csv       # Summary stats from aggregation
│   ├── empty_bins_hist.png          # Histogram of empty bins
│   ├── collisions_hist.png          # Histogram of collisions
│   └── max_load_hist.png            # Histogram of max load
├── README.md
└── requirements.txt
```

---

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Run the Simulation:
```bash
python scripts/01_run_simulation.py
```

### 3. Aggregate the Results:
```bash
python scripts/02_aggregate_results.py
```

### 4. Visualize the Output:
```bash
python scripts/03_visualize_results.py
```

---

## Requirements
- Python 3.7+
- pandas
- matplotlib
```
pandas
matplotlib
```