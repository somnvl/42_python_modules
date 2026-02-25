#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   GameEngine.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:21:39 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:52:57 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Game engine orchestrator for DataDeck."""

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates card creation and turn simulation."""

    def __init__(self) -> None:
        """Initialize engine with no factory or strategy."""
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configure the engine with a factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate a turn using current factory and strategy."""
        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell()
        ]
        self.cards_created = len(hand)
        result = self.strategy.execute_turn(hand, [])

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": result,
        }

    def get_engine_status(self) -> dict:
        """Return current engine statistics."""
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy
            else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
