#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/05 05:10:17 by somenvie            #+#    #+#            #
#   Updated: 2026/02/05 05:10:18 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Demonstrates different Python exception types and handling strategies."""


def garden_operations() -> None:
    """Demonstrates common error types."""

    # ValueError
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    # ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    # FileNotFoundError
    print("Testing FileNotFoundError...")
    file = "missing.txt"
    try:
        open(file)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}'\n")

    # KeyError
    print("Testing KeyError...")
    try:
        garden = {"tomato": "red"}
        garden["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:
    """Tests multiple error handling with single except block."""
    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    try:
        print("=== Garden Error Types Demo ===\n")
        test_error_types()
        print("All error types tested successfully!")
    except Exception as e:
        print(f"\nCritical error: {type(e).__name__}: {e}")
