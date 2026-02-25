#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Deck.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 15:29:10 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 01:57:19 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Deck management system for DataDeck."""

import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Manages a collection of cards of any type."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name. Return True if found, False otherwise."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw and return the top card of the deck."""
        card = self.cards[0]
        self.cards.remove(card)
        return card

    def get_deck_stats(self) -> dict:
        """Return stats about the deck's composition and average cost."""
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

        avg_cost = (
            sum(card.cost for card in self.cards) / len(self.cards)
            if self.cards
            else 0
        )
        return {
            "total_cards": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
