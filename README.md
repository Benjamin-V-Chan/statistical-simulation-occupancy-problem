# statistical-simulation-occupancy-problem

## Project Overview

This project simulates the classical **occupancy problem** in probability theory and statistics. The problem explores how randomly assigning $n$ indistinguishable or distinguishable balls into $m$ distinguishable bins leads to various distribution patterns. This project empirically investigates metrics such as the number of **empty bins**, the number of **collisions** (bins with more than one ball), and the **maximum load** (maximum number of balls in any single bin).

### Mathematical Foundations

Let $m$ be the number of bins and $n$ be the number of balls. Each ball is independently placed into one of the $m$ bins with equal probability $\frac{1}{m}$.

#### 1. Expected Number of Empty Bins
Let $X_i$ be the indicator random variable for the $i$-th bin being empty. Then:
$$E[X_i] = P(\text{bin } i \text{ is empty}) = \left(1 - \frac{1}{m}\right)^n$$

Therefore, the expected number of empty bins $E[E_m]$ is:
$$E[E_m] = \sum_{i=1}^{m} E[X_i] = m \left(1 - \frac{1}{m}\right)^n$$

#### 2. Expected Number of Collisions
Let $C$ be the number of bins with at least two balls. Let $X_i$ be the number of balls in bin $i$.
The expected number of collisions (bins with $X_i \geq 2$) is approximated by:
$$E[C] \approx m - E[E_m] - E[\text{singleton bins}]$$
where the expected number of singleton bins is:
$$E[\text{singleton}] = m \cdot \binom{n}{1} \left(\frac{1}{m}\right) \left(1 - \frac{1}{m}\right)^{n-1} = n \left(1 - \frac{1}{m}\right)^{n-1}$$

Thus,
$$E[C] \approx m - m\left(1 - \frac{1}{m}\right)^n - n \left(1 - \frac{1}{m}\right)^{n-1}$$

#### 3. Maximum Load (Balls in the Most Loaded Bin)
The maximum load $L_{\max}$ is a well-studied result in probability. For $n$ balls into $m$ bins, the maximum load with high probability is:
$$L_{\max} = \frac{\ln m}{\ln \left(\frac{m}{m - 1}\right)} \approx \frac{\ln m}{\ln \ln m} \quad \text{when } n = m$$
For $n > m$, the problem is modeled using Poisson distributions. Specifically:
$$P(X_i = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad \lambda = \frac{n}{m}$$
The tail behavior of the Poisson distribution helps estimate the likelihood of large loads.

The simulation in this project empirically validates these analytical results.

---

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