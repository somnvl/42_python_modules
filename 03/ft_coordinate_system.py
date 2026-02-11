#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:19 by somenvie            #+#    #+#            #
#   Updated: 2026/02/11 03:39:20 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Position Tracker - Exercise 2: 3D coordinates with tuples"""

import math


def parsing(coord_str: str) -> tuple:
    """Parse 'x,y,z' string to (x, y, z) tuple"""
    try:
        coord = coord_str.split(",")
        return (int(coord[0]), int(coord[1]), int(coord[2]))
    except (ValueError, IndexError):
        raise ValueError(
            f"invalid literal for int() with base 10: '{coord[0]}'")


def distance(origin: tuple, pos: tuple) -> None:
    """Calculate 3D Euclidean distance between two positions"""
    x1, y1, z1 = origin
    x2, y2, z2 = pos
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {origin} and {pos}: {dist:.2f}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    dist = distance(origin, pos)

    pos = "3,4,0"
    print(f'Parsing coordinates: "{pos}"')
    parsed = parsing(pos)
    print(f"Parsed position: {parsed}")
    dist = distance(origin, parsed)

    pos = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{pos}"')
    try:
        parsing(pos)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
