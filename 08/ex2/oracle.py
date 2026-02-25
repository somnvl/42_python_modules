#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 15:03:35 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 18:24:35 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os
from dotenv import load_dotenv


def load_config() -> dict:
    """Load configuration from .env file and environment variables."""
    try:
        load_dotenv()
        return {
            "MATRIX_MODE": os.environ.get("MATRIX_MODE"),
            "DATABASE_URL": os.environ.get("DATABASE_URL"),
            "API_KEY": os.environ.get("API_KEY"),
            "LOG_LEVEL": os.environ.get("LOG_LEVEL"),
            "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT"),
        }
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)


def check_config(config: dict) -> bool:
    """Check that all required config variables are set."""
    try:
        all_ok = True
        for key, value in config.items():
            if value is None:
                print(f"[WARNING] {key} is not set")
                all_ok = False
        return all_ok
    except Exception as e:
        print(f"Error checking config: {e}")
        return False


def display_config(config: dict) -> None:
    """Display the loaded configuration."""
    try:
        print("Configuration loaded:")
        for key, value in config.items():
            if key == "API_KEY":
                if key == "API_KEY":
                    print(f"  API_KEY: {'****' if value else 'not set'}")
            else:
                print(f"  {key}: {value or 'not set'}")
    except Exception as e:
        print(f"Error displaying config: {e}")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    check_config(config)
    display_config(config)
    print("\nThe Oracle sees all configurations.")
