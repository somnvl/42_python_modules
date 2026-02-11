#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:30 by somenvie            #+#    #+#            #
#   Updated: 2026/02/11 03:39:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Inventory Master - Exercise 4: Manage game inventory with dicts"""

import sys


def parsing() -> dict:
    """Parse command line arguments and build inventory dictionary"""
    if len(sys.argv) == 1:
        raise ValueError("Usage: ./ft_inventory_system.py <item:qty> ...")

    inventory = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            raise ValueError(f"Invalid format '{arg}'. Use item:quantity")
        item, qty = arg.split(":")

        if not qty.isdigit():
            raise ValueError(f"Quantity must be a number, got '{qty}'")
        inventory[item] = int(qty)

    return inventory


def get_quantity(item_tuple: tuple) -> int:
    """Extract quantity from (item_name, quantity) tuple"""
    return item_tuple[1]


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    try:
        inventory = parsing()

        # 1. Total items and unique types
        total_items = sum(inventory.values())
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
            percentage = (qty / total_items) * 100
            unit = "unit" if qty == 1 else "units"
            print(f"{item}: {qty} {unit} ({percentage:.1f}%)")

        # 3. Statistics
        print("\n=== Inventory Statistics ===")
        most_abundant = max(inventory.items(), key=get_quantity)
        least_abundant = min(inventory.items(), key=get_quantity)
        print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
        print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} units)\n")

        # 4. Categorize items
        print("\n=== Item Categories ===")
        moderate = {k: v for k, v in inventory.items() if v >= 3}
        scarce = {k: v for k, v in inventory.items() if v < 3}
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}\n")

        # 5. Management suggestions
        print("\n=== Management Suggestions ===")
        restock = [item for item, qty in inventory.items() if qty == 1]
        print(f"Restock needed: {restock}\n")

        # 6. Dictionary properties demo
        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        print(f"Dictionary values: {list(inventory.values())}")
        sample_item = list(inventory.keys())[0]
        print(
            f"Sample lookup - '{sample_item}' in inventory: {sample_item in inventory}"
        )

    except ValueError as e:
        print(f"Error: {e}")
