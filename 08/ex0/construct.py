#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 18:40:31 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 18:42:44 by somenvie           ###   ########.fr      #
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


def is_venv() -> bool:
    """
    Return True if running inside a virtual environment.
    In a virtual environment, sys.prefix differs from sys.base_prefix.
    """
    return sys.prefix != sys.base_prefix


def get_site_packages_path() -> str:
    """
    Return the primary site-packages installation path.
    """
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
        return "Unavailable"
    except Exception:
        return "Unavailable"


def display_inside_venv() -> None:
    """
    Display information when running inside a virtual environment.
    """
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    packages_path = get_site_packages_path()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    print("Environment comparison:")
    print(f"Base prefix (global Python): {sys.base_prefix}")
    print(f"Current prefix (virtual env): {sys.prefix}\n")

    print("Package installation path:")
    print(packages_path)


def display_outside_venv() -> None:
    """
    Display warning and instructions when not in a virtual environment.
    """
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("Environment comparison:")
    print(f"Base prefix (global Python): {sys.base_prefix}")
    print(f"Current prefix: {sys.prefix}\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("\nThen run this program again.")


if __name__ == "__main__":
    if is_venv():
        display_inside_venv()
    else:
        display_outside_venv()

"""
./construct.py
python3 -m venv matrix_env
source matrix_env/bin/activate

./construct.py
deactivate
"""
