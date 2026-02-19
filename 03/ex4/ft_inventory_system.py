#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 17:25:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/19 12:48:26 by somenvie           ###   ########.fr      #
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
        printed = {}
        while len(printed) < len(inventory):
            max_qty = -1
            max_item = ""
            for item, qty in inventory.items():
                if item not in printed and qty > max_qty:
                    max_qty = qty
                    max_item = item
            printed[max_item] = max_qty
            percentage = (max_qty / total_items) * 100 if total_items else 0.0
            unit = "unit" if max_qty == 1 else "units"
            print(f"{max_item}: {max_qty} {unit} ({percentage:.1f}%)")

        # 3. Statistics
        print("\n=== Inventory Statistics ===")
        max_qty = -1
        min_qty = -1
        max_item = ""
        min_item = ""
        for item, qty in inventory.items():
            if qty > max_qty:
                max_qty = qty
                max_item = item
            if min_qty == -1 or qty < min_qty:
                min_qty = qty
                min_item = item

        print(f"Most abundant: {max_item} ({max_qty} units)")
        unit = "unit" if min_qty == 1 else "units"
        print(f"Least abundant: {min_item} ({min_qty} {unit})")

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
        restock = ""
        for item, qty in inventory.items():
            if qty <= 1:
                if restock:
                    restock += ", "
                restock += item
        print(f"Restock needed: {restock}")

        # 6. Dictionary properties demo
        print("\n=== Dictionary Properties Demo ===")
        keys_str = ""
        for key in inventory.keys():
            if keys_str:
                keys_str += ", "
            keys_str += key
        print(f"Dictionary keys: {keys_str}")

        vals_str = ""
        for val in inventory.values():
            if vals_str:
                vals_str += ", "
            vals_str += str(val)
        print(f"Dictionary values: {vals_str}")

        sample_item = ""
        for key in inventory.keys():
            sample_item = key
            break
        print(
            f"Sample lookup - '{sample_item}' in inventory: "
            f"{sample_item in inventory}"
        )

    except ValueError as e:
        print(f"Error: {e}")
