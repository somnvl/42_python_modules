#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   CardFactory.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:19:45 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:19:54 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract factory interface for creating cards in DataDeck."""

from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed card sets."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a creature card."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a spell card."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create and return an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of given size and return its contents."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return the card types supported by this factory."""
        pass
