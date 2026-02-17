#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 18:14:44 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 18:15:43 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""
Data Alchemist - Exercise 6
Transform data with comprehensions
"""

if __name__ == "__main__":
    scores = [2300, 1800, 2150, 2050]
    players = ["alice", "bob", "charlie", "diana"]

    player_data = {
        "alice": {
            "score": 2300,
            "level": 15,
            "achievements": ["first_kill"],
        },
        "bob": {
            "score": 1800,
            "level": 12,
            "achievements": ["level_10"],
        },
        "charlie": {
            "score": 2150,
            "level": 14,
            "achievements": ["level_10"],
        },
        "diana": {
            "score": 2050,
            "level": 10,
            "achievements": ["boss_slayer"],
        },
    }

    # Keep player_data scores consistent with `scores` + `players`
    for i in range(len(players)):
        player_data[players[i]]["score"] = scores[i]

    print("=== Game Analytics Dashboard ===\n")

    print("--- List Comprehension Examples ---")

    high_scorers = [p for p in players if player_data[p]["score"] >= 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [s * 2 for s in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p for p in players if player_data[p]["level"] >= 12]
    print(f"Active players: {active_players}\n")

    print("--- Dict Comprehension Examples ---")

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

    print("--- Set Comprehension Examples ---")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        a for p in players for a in player_data[p]["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_region = {
        "north" if player_data[p]["level"] >= 15 else "south"
        for p in active_players
    }
    print(f"Active region: {active_region}\n")

    print("--- Combined Analysis ---")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = sum(scores) / len(scores) if scores else 0
    print(f"Average score: {average_score}")

    top = max(player_scores, key=lambda k: player_scores[k])
    top_score = player_scores[top]
    top_achievements = len(player_data[top]["achievements"])

    print(
        f"Top performer: {top} "
        f"({top_score} points, {top_achievements} achievements)"
    )
