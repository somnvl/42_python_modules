#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/05 05:10:35 by somenvie            #+#    #+#            #
#   Updated: 2026/02/05 05:10:36 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Simple garden management system using custom errors and cleanup."""


class GardenError(Exception):
    """Base error for garden-related problems."""

    pass


class InputError(GardenError):
    """Error for plant-related problems."""

    pass


class WaterError(GardenError):
    """Error for watering-related problems."""

    pass


class GardenManager:
    """Manages a simple list of plants and their state."""

    def __init__(self) -> None:
        """Initializes garden with an empty plant list."""
        self.plants: list[tuple[str, int, int]] = []

    def add_plants(self, plants: list[tuple[str, int, int]]) -> None:
        """Adds multiple plants, raising PlantError on bad input."""
        print("Adding plants to garden...")
        for name, water, sun in plants:
            if not name:
                raise InputError("Plant name cannot be empty!")
            if water is None:
                raise InputError("Plant water level cannot be empty!")
            if sun is None:
                raise InputError("Plant sunlight hours cannot be empty!")
            self.plants.append((name, water, sun))
            print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Raises GardenError if any plant is already at max water."""
        print("Watering plants...")
        print("Opening watering system")
        if not self.plants:
            raise GardenError("No plants to water.")
        for name, _, _ in self.plants:
            print(f"Watering {name} - success")

    def check_plant_health(self) -> None:
        """Checks health of all plants and reports errors."""
        print("Checking plant health...")
        if not self.plants:
            raise GardenError("No plants to check.")
        for name, water, sun in self.plants:
            try:
                if water < 1:
                    raise WaterError(
                        f"Water level {water} is too low (min 1)")
                if water > 10:
                    raise WaterError(
                        f"Water level {water} is too high (max 10)")
                if sun < 2:
                    raise WaterError(
                        f"Sunlight hours {sun} is too low (min 2)")
                if sun > 12:
                    raise WaterError(
                        f"Sunlight hours {sun} is too high (max 12)")
                print(f"{name}: healthy (water: {water}, sun: {sun})")
            except GardenError as e:
                print(f"Error checking {name}: {e}")

    def error_recovery(self, trigger_error: bool) -> None:
        """Simulates a garden error for recovery testing."""
        print("\nTesting error recovery...")
        if trigger_error:
            raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    """Runs full garden management demo with errors."""
    manager = GardenManager()

    try:
        manager.add_plants([("tomato", 5, 8), ("lettuce", 15, 8), ("", 0, 0)])
    except GardenError as e:
        print(f"Error adding plant: {e}\n")

    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Error while watering: {e}")
    finally:
        print("Closing watering system (cleanup)\n")

    try:
        manager.check_plant_health()
    except GardenError as e:
        print(f"Error while checking: {e}")

    try:
        manager.error_recovery(True)
        print("All good!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("===  Garden Management System ===\n")
    test_garden_management()
