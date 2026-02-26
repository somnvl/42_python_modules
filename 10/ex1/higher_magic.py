#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 03:06:03 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 04:08:01 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Higher magic: higher-order functions that operate on other functions."""

from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Return a new function that calls both spells and returns a tuple."""

    def combined(*args: Any) -> tuple:
        result1 = spell1(*args)
        result2 = spell2(*args)
        return (result1, result2)

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Return a new function that multiplies base_spell result"""

    def amplified(*args: Any) -> Any:
        return base_spell(*args) * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Return a function that casts spell only if condition is True."""

    def caster(*args: Any) -> Any:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """Return a function that casts all spells and returns list of results."""

    def sequence(*args: Any) -> list:
        return [spell(*args) for spell in spells]

    return sequence


if __name__ == "__main__":

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(target: str) -> int:
        return 10

    def is_enemy(target: str) -> bool:
        return target == "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print(f"Original: {damage('Dragon')}, Amplified: {mega('Dragon')}")
