#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   TournamentPlatform.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:58:35 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 03:06:15 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Tournament platform management system for DataDeck."""

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages card registrations, matches and leaderboard."""

    def __init__(self) -> None:
        """Initialize empty tournament platform."""
        self.cards: dict = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique ID."""
        card_id = f"{card.name.lower().replace(' ', '_')}_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards and update ratings."""
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        """Return cards sorted by rating descending."""
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda x: x[1].rating,
            reverse=True
        )
        return [
            {
                "rank": i + 1,
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}",
            }
            for i, (_, card) in enumerate(sorted_cards)
        ]

    def generate_tournament_report(self) -> dict:
        """Generate a full tournament report."""
        ratings = [c.rating for c in self.cards.values()]
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": sum(ratings) // len(ratings) if ratings else 0,
            "platform_status": "active",
        }
