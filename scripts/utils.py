import csv
import random

def set_seed(seed=42):
    random.seed(seed)

def save_dicts_to_csv(dict_list, filename):
    if not dict_list:
        return
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_list[0].keys())
        writer.writeheader()
        writer.writerows(dict_list)
