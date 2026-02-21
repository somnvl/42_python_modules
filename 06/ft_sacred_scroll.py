#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_sacred_scroll.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 21:43:02 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 22:57:53 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy
import alchemy.elements


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")
    try:
        print(
            "alchemy.create_earth(): "
            f"{alchemy.create_earth()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(
            "alchemy.create_air(): "
            f"{alchemy.create_air()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
