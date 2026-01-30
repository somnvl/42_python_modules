# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:26:23 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 22:06:26 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program that displays information for each garden plant through time."""


class Plant:
    """Represent a plant with name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def add_height(self, amount: int) -> None:
        """Increase the plant height by the given amount in cm."""
        self.height += amount

    def add_age(self, days: int) -> None:
        """Increase the plant age by the given number of days."""
        self.age += days

    def get_info(self) -> str:
        """Return a formatted description of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(plant.get_info())

    print("=== Day 7 ===")
    print(plant.get_info())
