#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 17:25:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 17:35:33 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Inventory Master - Exercise 4
Manage game inventory with dicts
"""

import sys


def parsing() -> dict:
    """Parse command line arguments and build inventory dictionary."""
    if len(sys.argv) == 1:
        raise ValueError("Usage: ./ft_inventory_system.py <item:qty> ...")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            raise ValueError(f"Invalid format '{arg}'. Use item:quantity")

        item, qty = arg.split(":", 1)

        if not qty.isdigit():
            raise ValueError(f"Quantity must be a number, got '{qty}'")

        inventory[item] = int(qty)

    return inventory


def get_quantity(item_tuple: tuple) -> int:
    """Extract quantity from (item_name, quantity) tuple."""
    return item_tuple[1]


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    try:
        inventory = parsing()

        # 1. Total items and unique types
        total_items = 0
        for qty in inventory.values():
            total_items += qty

        unique_types = len(inventory.keys())
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {unique_types}\n")

        # 2. Current inventory (sorted by quantity, descending)
        print("=== Current Inventory ===")
        sorted_items = sorted(
            inventory.items(),
            key=get_quantity,
            reverse=True,
        )

        for item, qty in sorted_items:
            if total_items == 0:
                percentage = 0.0
            else:
                percentage = (qty / total_items) * 100

            unit = "unit" if qty == 1 else "units"
            print(f"{item}: {qty} {unit} ({percentage:.1f}%)")

        # 3. Statistics
        print("\n=== Inventory Statistics ===")
        most_abundant = sorted_items[0]
        least_abundant = sorted_items[-1]

        print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")

        least_unit = "unit" if least_abundant[1] == 1 else "units"
        print(f"Least abundant: "
              f"{least_abundant[0]} ({least_abundant[1]} {least_unit})")

        # 4. Categorize items
        print("\n=== Item Categories ===")
        moderate = {}
        scarce = {}

        for item, qty in inventory.items():
            if qty > 3:
                moderate[item] = qty
            else:
                scarce[item] = qty

        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        # 5. Management suggestions
        print("\n=== Management Suggestions ===")
        restock = []

        for item, qty in inventory.items():
            if qty <= 1:
                restock.append(item)

        print(f"Restock needed: {', '.join(restock)}")

        # 6. Dictionary properties demo
        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {', '.join(inventory.keys())}")
        print(
            f"Dictionary values: "
            f"{', '.join(str(v) for v in inventory.values())}")

        sample_item = next(iter(inventory))
        print(
            f"Sample lookup - '{sample_item}' in inventory: "
            f"{sample_item in inventory}"
        )

    except ValueError as e:
        print(f"Error: {e}")
