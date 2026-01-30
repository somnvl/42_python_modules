#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:26:23 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 22:10:17 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program that displays information for each garden plant through time."""


class Plant:
    """Represent a plant with name, height and age."""

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, amount: int) -> None:
        """Increase the plant height by the given amount in cm."""
        self.height += amount

    def age(self, days: int) -> None:
        """Increase the plant age by the given number of days."""
        self.plant_age += days

    def get_info(self) -> str:
        """Return a formatted description of the plant."""
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Lily of the Valley", 10, 5),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    total_growth = 0
    for _ in range(6):
        for plant in plants:
            plant.grow(1)
            plant.age(1)
            total_growth += 1

    print()
    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())

    print()
    print(f"Growth this week: {total_growth}cm")
