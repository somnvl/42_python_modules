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

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self, amount: int) -> None:
        """Increase the plant height by the given amount in cm."""
        self.height += amount

    def age(self, days: int) -> None:
        """Increase the plant age by the given number of days."""
        self._age += days

    def get_info(self) -> str:
        """Return a formatted description of the plant."""
        return f"{self.name}: {self.height}cm, {self._age} days old"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Lily of the Valley", 10, 5),
    ]

    p = 0
    initial_height = plants[p].height

    print("=== Day 1 ===")
    print(plants[p].get_info())

    for _ in range(6):
        for plant in plants:
            plant.grow(1)
            plant.age(1)

    print("=== Day 7 ===")
    print(plants[p].get_info())

    growth = plants[p].height - initial_height
    print(f"Growth this week: +{growth}cm")
