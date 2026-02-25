#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 15:02:31 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 18:28:51 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Load and verify required packages, analyze simulated Matrix data,
and generate a visualization saved as matrix_analysis.png.
"""

from typing import Any
import sys
import importlib.util
import importlib.metadata


def check_dependencies() -> dict:
    """Check required packages and return their versions."""
    packages = ["pandas", "numpy", "matplotlib"]
    results = {}
    all_ok = True

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in packages:
        try:
            spec = importlib.util.find_spec(package)
            if spec is not None:
                version = importlib.metadata.version(package)
                print(f"[OK] {package} ({version})")
                results[package] = version
            else:
                print(f"[MISSING] {package} - run: pip install {package}")
                all_ok = False
        except Exception as e:
            print(f"[ERROR] {package}: {e}")
            all_ok = False

    if not all_ok:
        print("\nInstall missing packages and rerun.")
        sys.exit(1)

    return results


def analyze_data() -> Any:
    """Generate and analyze simulated Matrix data."""
    try:
        import pandas as pd
        import numpy as np

        np.random.seed(42)
        data = pd.DataFrame(
            {
                "time": np.arange(1000),
                "signal": np.random.randn(1000).cumsum(),
                "noise": np.random.uniform(-1, 1, 1000),
            }
        )
        print("\nAnalyzing Matrix data...")
        print(f"Processing {len(data)} data points...")
        return data
    except Exception as e:
        print(f"Error analyzing data: {e}")
        sys.exit(1)


def generate_plot(data: Any) -> None:
    """Generate and save a visualization of the Matrix data."""
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 5))
        plt.plot(data["time"], data["signal"], label="Signal")
        plt.plot(data["time"], data["noise"], label="Noise", alpha=0.4)
        plt.title("Matrix Data Analysis")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.legend()
        plt.tight_layout()
        plt.savefig("matrix_analysis.png")
        plt.close()
        print("Generating visualization...\n")
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(f"Error generating plot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    check_dependencies()
    data = analyze_data()
    generate_plot(data)

"""
python3 loading.py

python3 -m venv matrix_env
source matrix_env/bin/activate
pip install -r requirements.txt
python3 loading.py

deactivate
pip install poetry
poetry install
poetry run python3 loading.py
"""
