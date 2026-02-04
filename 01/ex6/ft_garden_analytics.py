#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:27:50 by somenvie            #+#    #+#            #
#   Updated: 2026/02/01 23:06:18 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program for comprehensive garden data analytics."""


class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height and age."""
        self.name = str.capitalize(name)
        self.height = height
        self.age = age

    def grow(self, amount: int) -> None:
        """Make the plant grow by a specified amount."""
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that can produce flowers."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flowering plant with color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Make the plant bloom."""
        return "(blooming)"

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.color} flowers {self.bloom()}"


class PrizeFlower(FloweringPlant):
    """Prize-winning flower with points."""

    def __init__(
        self, name: str, height: int, age: int, color: str, prize_points: int
    ) -> None:
        """Initialize a prize flower with points."""
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class Garden:
    """Represents a garden containing plants."""

    def __init__(self, name: str) -> None:
        """Initialize a garden with a name."""
        self.name = str.capitalize(name)
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self, amount: int) -> None:
        """Make all plants in the garden grow."""
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)


class GardenManager:
    """Manages multiple gardens."""

    def __init__(self) -> None:
        """Initialize the garden manager."""
        self.gardens = []

    def add_garden(self, name: str) -> None:
        """Add a new garden to the manager."""
        self.gardens.append(Garden(name))

    @classmethod
    def create_garden_network(cls, names: list) -> "GardenManager":
        """
        ** Create a manager with multiple gardens.
        ** Args: names -> List of garden names. Defaults to ["Alice", "Bob"].
        ** Returns: A GardenManager with the specified gardens.
        """
        manager = cls()
        for name in names:
            manager.add_garden(name)
        return manager


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.gardens[0]

    alice_garden.add_plant(Plant("oak tree", 100, 365))
    alice_garden.add_plant(FloweringPlant("rose", 25, 30, "red"))
    alice_garden.add_plant(PrizeFlower("sunflower", 50, 45, "yellow", 10))

    print()
    alice_garden.grow_all(1)
    print()
