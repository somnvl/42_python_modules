#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   AggressiveStrategy.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:20:21 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:54:48 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Aggressive strategy implementation for DataDeck."""

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Plays low-cost creatures first and attacks directly."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute turn by playing cheap cards and attacking."""
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        played = []
        mana_used = 0
        damage = 0
        mana_budget = 5

        for card in sorted_hand:
            if mana_used + card.cost <= mana_budget:
                played.append(card.name)
                mana_used += card.cost
                damage += getattr(card, "attack", 0) or card.cost

        targets = self.prioritize_targets(["Enemy Player"])

        return {
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        """Return strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Target enemy player directly first."""
        return available_targets
