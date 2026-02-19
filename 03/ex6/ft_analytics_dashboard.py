#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 18:14:44 by somenvie            #+#    #+#            #
#   Updated: 2026/02/19 12:51:48 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Data Alchemist - Exercise 6
Transform data with comprehensions
"""


def get_score(player_tuple: tuple) -> int:
    """Extract score from (player_name, score) tuple."""
    return player_tuple[1]


if __name__ == "__main__":
    player_data = {
        "alice": {
            "score": 2300,
            "level": 15,
            "achievements": ["first_kill", "speed_demon", "boss_slayer",
                             "level_10", "treasure_hunter"],
        },
        "bob": {
            "score": 1800,
            "level": 12,
            "achievements": ["level_10", "first_kill", "collector"],
        },
        "charlie": {
            "score": 2150,
            "level": 14,
            "achievements": ["level_10", "boss_slayer", "treasure_hunter",
                             "speed_demon", "perfectionist", "collector",
                             "first_kill"],
        },
        "diana": {
            "score": 2050,
            "level": 10,
            "achievements": ["boss_slayer", "level_10", "first_kill",
                             "treasure_hunter"],
        },
    }

    players = [p for p in player_data.keys()]
    scores = [player_data[p]["score"] for p in player_data.keys()]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    high_scorers = [p for p in players if player_data[p]["score"] >= 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s * 2 for s in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p for p in players if player_data[p]["level"] >= 12]
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")

    player_scores = {p: player_data[p]["score"] for p in players}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([p for p in players if player_data[p]["score"] >= 2000]),
        "medium": len([
            p for p in players
            if 1800 <= player_data[p]["score"] < 2000
        ]),
        "low": len([p for p in players if player_data[p]["score"] < 1800]),
    }
    print(f"Score categories: {score_categories}")

    counts = {p: len(player_data[p]["achievements"]) for p in players}
    print(f"Achievement counts: {counts}\n")

    print("=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        a for p in players for a in player_data[p]["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {
        "north" if player_data[p]["level"] >= 15 else "south"
        for p in active_players
    }
    print(f"Active regions: {active_regions}\n")

    print("=== Combined Analysis ===")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = sum(scores) / len(scores) if scores else 0
    print(f"Average score: {average_score}")

    top = max(player_scores.items(), key=get_score)
    print(
        f"Top performer: {top[0]} "
        f"({top[1]} points, {counts[top[0]]} achievements)"
    )
