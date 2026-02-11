#!/usr/bin/env python3


# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_raise_errors.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/10 19:52:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/10 19:52:52 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Raises validation errors for plant health checks."""


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> None:
    """Validates plant name, water level, and sunlight hours."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """Tests plant health checks with valid and invalid values."""
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error: {e}\n")

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}\n")

    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}\n")

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    print("===  Garden Plant Health Checker ===\n")
    test_plant_checks()
