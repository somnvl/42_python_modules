#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:58:33 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 03:02:33 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Demonstration script for the DataDeck tournament platform."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Run the tournament platform demonstration."""
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 6, 1150)

    print("Registering Tournament Cards...")
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        print(f"\n{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        card = list(platform.cards.values())[entry['rank'] - 1]
        print(
            f"{entry['rank']}. {entry['name']} "
            f"- Rating: {entry['rating']} "
            f"({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
