#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Combatable.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:05:32 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:58:09 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract combat interface for DataDeck."""

from abc import ABC, abstractmethod


class Combatable(ABC):
    """Interface for cards with combat capabilities."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target and return combat result."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage and return result."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return current combat statistics."""
        pass
