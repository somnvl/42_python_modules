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

"""Program demonstrating data protection through encapsulation."""


class SecurePlant:
    """Represent a plant with name, height and age, with protected data"""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        """Return height."""
        return self._height

    def set_height(self, height: int) -> None:
        """Set height with validation."""
        if height < 0:
            print()
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def get_age(self) -> int:
        """Return age."""
        return self._age

    def set_age(self, age: int) -> None:
        """Set age with validation."""
        if age < 0:
            print()
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_info(self) -> str:
        """Return a formatted description of the plant."""
        return f"{self.name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Lily of the Valley", 0, 0)
    print(f"Plant created: {plant.name}")

    plant.set_height(10)
    plant.set_age(5)

    plant.set_height(-5)
    print()
    print(f"Current plant: {plant.get_info()}")
