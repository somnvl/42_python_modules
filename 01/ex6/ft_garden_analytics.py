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
        self.name = str.title(name)
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

    @staticmethod
    def bloom() -> str:
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

    _validate = 0

    def __init__(self, name: str) -> None:
        """Initialize a garden with a name."""
        self.name = str.title(name)
        self.plants = []
        self.growth = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        if not GardenManager.validate_height(plant.height):
            print(f"Error: Invalid height ({plant.height}) !")
            self._validate = 1
        else:
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self, amount: int) -> None:
        """Make all plants in the garden grow."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.growth += amount

    def get_report(self) -> None:
        """Display a detailed report of the garden."""
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")

        regular_count = 0
        flowering_count = 0
        prize_count = 0

        for plant in self.plants:
            print(f"- {plant}")

            if plant.__class__ == Plant:
                regular_count += 1
            elif plant.__class__ == FloweringPlant:
                flowering_count += 1
            elif plant.__class__ == PrizeFlower:
                prize_count += 1

        total_count = regular_count + flowering_count + prize_count
        print(f"\nPlants added: {total_count}, Total growth: {self.growth}cm")
        print(
            f"Plant types: {regular_count} regular, "
            f"{flowering_count} flowering, {prize_count} prize flowers"
        )


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
        """Create a manager with multiple gardens."""
        manager = cls()
        for name in names:
            manager.add_garden(name)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate if the height value is positive."""
        return height >= 0

    class GardenStats:
        """Helper class for calculating garden statistics."""

        def __init__(self, manager: "GardenManager") -> None:
            self.manager = manager

        def error_check(self) -> str:
            """Check if any garden has validation errors."""
            for garden in self.manager.gardens:
                if garden._validate == 1:
                    return "\nHeight validation test: False"
            return "\nHeight validation test: True"

        def garden_scores(self) -> str:
            """Display garden scores."""
            result = "Garden scores - "
            garden_count = 0

            for garden in self.manager.gardens:
                score = garden.growth * 10

                for plant in garden.plants:
                    score += plant.height

                    if plant.__class__ == PrizeFlower:
                        score += plant.prize_points

                if garden_count > 0:
                    result += ", "

                result += f"{garden.name}: {score}"
                garden_count += 1

            return result

        def total_gardens(self) -> str:
            """Count total gardens."""
            total_gardens = 0
            for _ in self.manager.gardens:
                total_gardens += 1
            return f"Total gardens managed: {total_gardens}"

        def garden_stats(self) -> None:
            """Display all garden statistics."""
            print(f"{self.error_check()}")
            print(f"{self.garden_scores()}")
            print(f"{self.total_gardens()}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice = manager.gardens[0]
    alice.add_plant(Plant("oak tree", 100, 365))
    alice.add_plant(FloweringPlant("rose", 25, 30, "red"))
    alice.add_plant(PrizeFlower("sunflower", 50, 45, "yellow", 10))
    alice.grow_all(1)
    alice.get_report()

    bob = manager.gardens[1]
    bob.plants = [
        Plant("oak tree", 70, 95),
        FloweringPlant("rose", 22, 26, "red")
    ]

    stats = GardenManager.GardenStats(manager)
    stats.garden_stats()
