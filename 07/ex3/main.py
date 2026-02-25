#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:22:11 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:49:16 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Demonstration script for the DataDeck game engine."""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Run the game engine demonstration."""
    print("\n=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    display_factory = FantasyCardFactory()
    dragon = display_factory.create_creature("dragon")
    goblin = display_factory.create_creature("goblin")
    bolt = display_factory.create_spell()
    print(
        f"Hand: [{dragon.name} ({dragon.cost}), "
        f"{goblin.name} ({goblin.cost}), "
        f"{bolt.name} ({bolt.cost})]"
    )

    print("\nTurn execution:")
    result = engine.simulate_turn()
    print(f"Strategy: {result['strategy']}")
    print(f"Actions: {result['actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexi achieved!")


if __name__ == "__main__":
    main()
