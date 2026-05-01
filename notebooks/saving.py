import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib


def setup_folders():
    folders = [
        "data",
        "data/raw",
        "data/processed",
        "plots",
        "models",
        "results"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def save_dataset(df, name, folder="data/processed"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}.csv")
    df.to_csv(path, index=False)
    print(f"Saved: {path}")


def save_model(model, name, folder="models"):
    path = f"{folder}/{name}.pkl"
    joblib.dump(model, path)


def save_figure(name, folder="plots", dpi=300):
    path = f"{folder}/{name}.png"
    plt.savefig(path, dpi=dpi, bbox_inches="tight")

def save_results(results, name, folder="results"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}.csv")

    results.to_csv(path)