#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Rankable.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:57:50 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:58:56 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Abstract ranking interface for DataDeck tournament system."""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """Interface for cards that can be ranked in tournaments."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return current ranking information."""
        pass
