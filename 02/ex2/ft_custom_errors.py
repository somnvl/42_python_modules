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

"""Defines custom garden-related exception types and demo tests."""


class GardenError(Exception):
    """Base exception for garden-related problems."""

    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""

    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""

    pass


def check_plant(plant: str, age: int) -> None:
    """Raises PlantError if plant age is too high."""
    if age >= 10:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(water: int) -> None:
    """Raises WaterError if water level is too low."""
    if water <= 2:
        raise WaterError("Not enough water in the tank!")


def test_plant_error(plant: str, age: int) -> None:
    """Tests raising and catching PlantError."""
    print("\nTesting PlantError...")
    try:
        check_plant(plant, age)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error(water: int) -> None:
    """Tests raising and catching WaterError."""
    print("\nTesting WaterError...")
    try:
        check_water(water)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors(plant: str, age: int, water: int) -> None:
    """Tests catching all garden errors via GardenError."""
    print("\nTesting catching all garden errors...")

    try:
        check_plant(plant, age)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(water)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant_error("tomato", 100)
    test_water_error(0)
    test_all_garden_errors("tomato", 100, 0)
    print("\nAll custom error types work correctly!")
