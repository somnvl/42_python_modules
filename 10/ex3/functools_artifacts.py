#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 03:06:03 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 04:16:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""Functools artifacts: reduce, partial, lru_cache, singledispatch."""

import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the given operation."""
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b),
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Return specialized enchantment functions using functools.partial."""
    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")
    lightning = functools.partial(
        base_enchantment, power=50, element="lightning"
    )
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return nth fibonacci number using lru_cache for memoization."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Return a singledispatch function handling int, str and list."""

    @functools.singledispatch
    def cast(arg: object) -> str:
        return f"Unknown spell type: {type(arg)}"

    @cast.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage points"

    @cast.register(str)
    def _(arg: str) -> str:
        return f"Enchantment spell: {arg}"

    @cast.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells cast"

    return cast


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    def base_enchant(power: int, element: str, target: str) -> str:
        """Apply enchantment to target."""
        return f"{element} enchantment on {target} with power {power}"

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
