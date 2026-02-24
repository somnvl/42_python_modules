#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_circular_curse.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 15:31:45 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 16:36:29 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(
        f'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )
    print()

    print("Testing spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')
    print()

    print("Testing late import technique:")
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
