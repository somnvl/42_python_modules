#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_import_transmutation.py                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 23:01:36 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 15:24:20 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")
    print()
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")
    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
