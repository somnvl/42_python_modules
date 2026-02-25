#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 15:02:13 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 16:24:13 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Detect and display information about the current Python environment.

Shows whether the script runs inside a virtual environment or not,
and provides setup instructions when no virtual environment is active.
"""

import sys
import os
import site


def is_in_venv() -> bool:
    """Return True if running inside a virtual environment."""
    try:
        if sys.prefix != sys.base_prefix:
            return True
        return False
    except Exception as e:
        print(f"Error during venv detection: {e}")
        return False


def get_venv_info() -> dict:
    """Return name, path and site-packages path of the active virtual env."""
    try:
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        packages_path = site.getsitepackages()[0]
        return {
            "name": venv_name,
            "path": venv_path,
            "packages": packages_path,
        }
    except Exception as e:
        print(f"Error retrieving venv info: {e}")
        return {}


def display_inside_venv(info: dict) -> None:
    """Print details of the active virtual environment."""
    try:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {info['name']}")
        print(f"Environment Path: {info['path']}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage installation path:\n{info['packages']}")
    except Exception as e:
        print(f"Error displaying venv info: {e}")


def display_outside_venv() -> None:
    """Print a warning and setup instructions when no virtual env is active."""
    try:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")
        print("\nThen run this program again.")
    except Exception as e:
        print(f"Error displaying outside info: {e}")


if __name__ == "__main__":
    if is_in_venv():
        display_inside_venv(get_venv_info())
    else:
        display_outside_venv()
