#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 05:27:29 by somenvie            #+#    #+#            #
#   Updated: 2026/02/01 21:41:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Program demonstrating inheritance with specialized plant types."""


class Plant:
    """Base class representing a plant with common attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return basic plant information."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


class Flower(Plant):
    """A flowering plant with color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Make the flower bloom."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """Return flower information with color."""
        return (
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """A tree with trunk diameter attribute."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """Initialize a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display shade production."""
        amount = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {amount} square meters of shade")

    def get_info(self) -> str:
        """Return tree information with trunk diameter."""
        return (
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """A vegetable with harvest season and nutritional value."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Initialize a vegetable with harvest season and nutritional value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """Return vegetable information with harvest season."""
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 80, 45, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 730, 30),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 120, "autumn", "vitamin A"),
    ]

    for flower in flowers:
        print(flower.get_info())
        flower.bloom()
        print()

    for tree in trees:
        print(tree.get_info())
        tree.produce_shade()
        print()

    for vegetable in vegetables:
        print(vegetable.get_info())
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")
        print()
