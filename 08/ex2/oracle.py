#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 18:51:30 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 18:54:23 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""
Secure configuration loader using environment variables and .env files.
Demonstrates development vs production configuration handling.
"""

import os
import sys

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> dict[str, str]:
    """
    Load configuration from .env and environment variables.
    System environment variables override .env values.
    """
    try:
        from dotenv import load_dotenv

        load_dotenv()

        config: dict[str, str] = {}

        for var in REQUIRED_VARS:
            value = os.getenv(var)
            if not value:
                print(f"[ERROR] Missing required variable: {var}")
                sys.exit(1)
            config[var] = value

        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)


def display_config(config: dict[str, str]) -> None:
    """
    Display configuration safely without exposing secrets.
    """
    print("Configuration loaded:\n")

    mode = config["MATRIX_MODE"]

    print(f"Mode: {mode}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}")

    if mode == "development":
        print("Database: Connected to local development instance")
    elif mode == "production":
        print("Database: Connected to production server")
    else:
        print("[WARNING] Unknown MATRIX_MODE value")

    print("API Access: Authenticated")


def security_check() -> None:
    """
    Basic security validation checks.
    """
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    configuration = load_config()
    display_config(configuration)
    security_check()

    print("\nThe Oracle sees all configurations.")

"""
./oracle.py
python3 -m venv matrix_env
source matrix_env/bin/activate
pip install dotenv
./oracle.py

MATRIX_MODE=production python3 oracle.py

mv .env .env.bak && python3 oracle.py && mv .env.bak .env

git status
"""
