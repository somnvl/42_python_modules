#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   CreatureCard.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 17:46:25 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:15:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Concrete CreatureCard implementation for DataDeck."""

from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    """A card representing a creature with attack and health."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        """Initialize creature with attack and health (must be > 0)."""
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers.")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Summon the creature to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def get_card_info(self) -> Dict:
        """Return card info extended with type, attack and health."""
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target) -> dict:
        """Attack a target and return combat result."""
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
