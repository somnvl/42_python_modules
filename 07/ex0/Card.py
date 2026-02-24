#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Card.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 17:45:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 17:46:03 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class for all cards in DataDeck."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card and return the result."""
        pass

    def get_card_info(self) -> Dict:
        """Return basic card information."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with the available mana."""
        return available_mana >= self.cost
