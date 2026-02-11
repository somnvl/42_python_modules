#!/usr/bin/env python3


# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/05 05:10:22 by somenvie            #+#    #+#            #
#   Updated: 2026/02/05 05:10:23 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Demonstrates use of finally for cleanup in a watering system."""


class InvalidPlant(Exception):
    """Raised when an invalid plant is encountered."""

    pass


def water_plants(plant_list: list) -> None:
    """Waters each plant in the provided list."""
    print("Opening watering system")
    for plant in plant_list:
        if not plant:
            raise InvalidPlant("Cannot water None - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system() -> None:
    """Tests watering in normal and error scenarios with cleanup."""
    error = 0
    try:
        print("\nTesting normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
    except InvalidPlant as e:
        print(f"Error: {e}")
        error = 1
    finally:
        print("Closing watering system (cleanup)")
    if error == 0:
        print("Watering completed successfully!")

    try:
        print("\nTesting with error...")
        water_plants(["tomato", "", "carrots"])
    except InvalidPlant as e:
        print(f"Error: {e}")
        error = 1
    finally:
        print("Closing watering system (cleanup)")
    if error == 0:
        print("Watering completed successfully!")


if __name__ == "__main__":
    print("===  Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
