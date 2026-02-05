#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:26:32 by somenvie            #+#    #+#            #
#   Updated: 2026/01/31 17:05:53 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program demonstrating streamlined plant creation."""


class Plant:
    """Represent a plant with name, height and age."""

    def __init__(self, name: str, height: int, _age: int) -> None:
        self.name = name
        self.height = height
        self._age = _age

    def grow(self, amount: int) -> None:
        """Increase the plant height by the given amount in cm."""
        self.height += amount

    def age(self, days: int) -> None:
        """Increase the plant age by the given number of days."""
        self._age += days

    def get_info(self) -> str:
        """Return a formatted description of the plant."""
        return f"Created: {self.name} ({self.height}cm, {self._age} days)"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")

    count = 0
    for plant in plants:
        print(plant.get_info())
        count += 1

    print()
    print(f"Total plants created: {count}")
