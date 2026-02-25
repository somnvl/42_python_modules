#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ArtifactCard.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 15:28:41 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:57:16 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Concrete ArtifactCard implementation for DataDeck."""

from ex0.Card import Card


class ArtifactCard(Card):
    """A permanent card that stays in play until destroyed."""

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        """Initialize artifact with durability (must be > 0) and effect."""
        if durability <= 0:
            raise ValueError("Durability must be a positive integer.")
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Place the artifact on the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        """Activate the artifact's ongoing effect."""
        return {
            "artifact": self.name,
            "ability_activated": self.effect,
            "durability_remaining": self.durability,
        }
