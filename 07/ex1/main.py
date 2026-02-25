#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 15:29:06 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 15:14:57 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    deck.add_card(
        SpellCard(
            "Lightning Bolt",
            4,
            "Common",
            "Deal 3 damage to target",
        )
    )
    deck.add_card(
        ArtifactCard(
            "Mana Crystal",
            3,
            "Common",
            5,
            "+1 mana per turn")
    )
    deck.add_card(
        CreatureCard(
            "Fire Dragon",
            5,
            "Legendary",
            7,
            5)
    )

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    game_state = {"turn": 1}

    while deck.cards:
        card = deck.draw_card()
        print(f"\nDrew: {card.name} ({type(card).__name__})")
        print(f"Play result: {card.play(game_state)}")

    print("\nPolymorphism in action: Same interface, different card behavior!")


if __name__ == "__main__":
    main()
