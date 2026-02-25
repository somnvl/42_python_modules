#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   GameStrategy.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:19:08 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:19:15 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract strategy interface for DataDeck game engine."""

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Defines how a player decides actions during their turn."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a full turn and return actions taken."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Return targets sorted by priority."""
        pass
