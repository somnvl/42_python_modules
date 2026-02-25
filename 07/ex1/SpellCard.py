#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   SpellCard.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 15:28:11 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:57:47 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Concrete SpellCard implementation for DataDeck."""

from ex0.Card import Card


class SpellCard(Card):
    """A one-time use card that applies an instant magical effect."""

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        """Initialize spell with its effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Cast the spell and consume it."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type,
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell effect on targets."""
        return {
            "spell": self.name,
            "targets": targets,
            "effect_applied": self.effect_type,
        }
