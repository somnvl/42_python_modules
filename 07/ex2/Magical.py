#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Magical.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:05:33 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:58:53 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract magic interface for DataDeck."""

from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for cards with magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on targets and return result."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana and return updated mana info."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return current magic statistics."""
        pass
