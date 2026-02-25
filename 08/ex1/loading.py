#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 18:44:55 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 18:46:39 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""
Load and verify required packages, analyze simulated Matrix data,
and generate a visualization saved as matrix_analysis.png.

Demonstrates dependency management and environment detection
(pip vs Poetry).
"""

import importlib.metadata
import importlib.util
import sys
from typing import Any


def detect_environment() -> None:
    """
    Display information about the current Python environment.
    Helps demonstrate pip vs Poetry environments.
    """
    print("Environment information:")
    print(f"Python executable: {sys.executable}")
    print(f"Environment prefix: {sys.prefix}")

    if sys.prefix != sys.base_prefix:
        print("Virtual environment detected.")
        if "poetry" in sys.prefix.lower():
            print("This environment appears to be managed by Poetry.\n")
        else:
            print("This environment may be manually created (pip/venv).\n")
    else:
        print("Running in global Python environment.\n")


def check_dependencies() -> dict[str, str]:
    """
    Check required packages and return their versions.
    Exit if any dependency is missing.
    """
    packages = ["pandas", "numpy", "matplotlib"]
    results: dict[str, str] = {}
    all_ok = True

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in packages:
        try:
            spec = importlib.util.find_spec(package)
            if spec is not None:
                version = importlib.metadata.version(package)
                print(f"[OK] {package} ({version}) - Ready")
                results[package] = version
            else:
                print(f"[MISSING] {package}")
                print(f"Install with: pip install {package}")
                all_ok = False
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {package}")
            print(f"Install with: pip install {package}")
            all_ok = False
        except Exception as error:
            print(f"[ERROR] {package}: {error}")
            all_ok = False

    if not all_ok:
        print("\nInstall missing dependencies and rerun.")
        sys.exit(1)

    print()
    return results


def analyze_data() -> Any:
    """
    Generate and analyze simulated Matrix data.
    """
    try:
        import numpy as np
        import pandas as pd

        np.random.seed(42)

        data = pd.DataFrame(
            {
                "time": np.arange(1000),
                "signal": np.random.randn(1000).cumsum(),
                "noise": np.random.uniform(-1, 1, 1000),
            }
        )

        print("Analyzing Matrix data...")
        print(f"Processing {len(data)} data points...\n")

        return data

    except Exception as error:
        print(f"Error analyzing data: {error}")
        sys.exit(1)


def generate_plot(data: Any) -> None:
    """
    Generate and save a visualization of the Matrix data.
    """
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

        print("Generating visualization...")
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as error:
        print(f"Error generating plot: {error}")
        sys.exit(1)


if __name__ == "__main__":
    detect_environment()
    check_dependencies()
    dataset = analyze_data()
    generate_plot(dataset)

"""
./loading.py

python3 -m venv matrix_env
source matrix_env/bin/activate
pip install -r requirements.txt
./loading.py

deactivate
pip install poetry
poetry install
poetry run ./loading.py
"""
