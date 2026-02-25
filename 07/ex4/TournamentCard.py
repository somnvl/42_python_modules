#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   TournamentCard.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 02:58:12 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 03:05:17 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""TournamentCard combining Card, Combatable and Rankable interfaces."""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card with combat and ranking capabilities for tournaments."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack: int, health: int, rating: int = 1200
    ) -> None:
        """Initialize tournament card with combat stats and base rating."""
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers.")
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """Summon the tournament card to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered the battlefield",
        }

    def attack(self, target) -> dict:
        """Attack a target and return combat result."""
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "combat_resolved": True,
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        blocked = min(self.attack_power // 2, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < self.health,
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics."""
        return {
            "name": self.name,
            "attack": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        """Calculate rating based on wins and losses."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Add wins and increase rating by 16 per win."""
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        """Add losses and decrease rating by 16 per loss."""
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        """Return current ranking information."""
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        """Return full tournament statistics."""
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "attack": self.attack_power,
            "health": self.health,
        }
