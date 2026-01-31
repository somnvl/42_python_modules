#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:27:04 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 05:27:05 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program demonstrating streamlined plant creation."""


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
        return f"Created: {self.name} ({self.height}cm, {self.plant_age} days)"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Lily of the Valley", 15, 120),
    ]

    print("=== Plant Factory Output ===")

    print()
    print(f"Current plant: {plants[0].get_info()}")
