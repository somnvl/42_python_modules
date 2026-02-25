#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Card.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 17:45:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:55:44 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract Card base class for DataDeck."""

from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract blueprint for all DataDeck cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize card with name, cost and rarity."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card — must be implemented by subclasses."""
        pass

    def get_card_info(self) -> Dict:
        """Return card's basic attributes as a dict."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return True if available_mana >= card cost."""
        return available_mana >= self.cost
