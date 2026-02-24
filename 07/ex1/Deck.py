#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Deck.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 15:29:10 by somenvie            #+#    #+#            #
#   Updated: 2026/02/24 17:48:03 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card = self.cards[0]
        self.cards.remove(card)
        return card

    def get_deck_stats(self) -> dict:
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
