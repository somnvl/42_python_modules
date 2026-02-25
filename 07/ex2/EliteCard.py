#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   EliteCard.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:05:28 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:58:32 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Elite card combining Card, Combatable and Magical interfaces."""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card implementing combat and magical capabilities."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, mana: int
    ) -> None:
        """Initialize elite card with attack power and mana pool."""
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """Place the elite card on the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card entered the battlefield",
        }

    def attack(self, target) -> dict:
        """Attack a target and return combat result."""
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        """Block part of incoming damage and return defense result."""
        blocked = min(self.attack_power // 2, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < 10,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on a list of targets."""
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": len(targets) + 2,
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel mana and add it to the mana pool."""
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_combat_stats(self) -> dict:
        """Return current combat statistics."""
        return {
            "name": self.name,
            "attack_power": self.attack_power,
        }

    def get_magic_stats(self) -> dict:
        """Return current magic statistics."""
        return {
            "name": self.name,
            "mana": self.mana,
        }
