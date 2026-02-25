#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   FantasyCardFactory.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:20:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:56:12 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Fantasy-themed card factory for DataDeck."""

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed cards: dragons, goblins, elemental spells."""

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> CreatureCard:
        """Create a fantasy creature (dragon or goblin)."""
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 5, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> SpellCard:
        """Create an elemental spell."""
        return SpellCard(
            "Lightning Bolt", 3, "Common", "Deal 3 damage to target"
        )

    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> ArtifactCard:
        """Create a magical artifact."""
        return ArtifactCard("Mana Ring", 2, "Rare", 3, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        """Create a fantasy deck of given size."""
        deck = [
            self.create_creature("goblin"),
            self.create_spell(),
            self.create_artifact()
        ]
        return {"deck": deck, "size": len(deck), "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        """Return supported card types."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
