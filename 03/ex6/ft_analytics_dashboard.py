#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 16:39:20 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 16:41:17 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Data Alchemist - Exercise 6
Transform data with comprehensions
"""

if __name__ == "__main__":
    scores = [2300, 1800, 2150, 1600, 2400, 1900]
    players = ["alice", "bob", "charlie", "diana", "eve", "frank"]

    player_data = {
        "alice": {"score": 2300, "level": 15, "achievements": 5},
        "bob": {"score": 1800, "level": 12, "achievements": 3},
        "charlie": {"score": 2150, "level": 14, "achievements": 7},
        "diana": {"score": 1600, "level": 10, "achievements": 2},
        "eve": {"score": 2400, "level": 18, "achievements": 9},
        "frank": {"score": 1900, "level": 13, "achievements": 4},
    }

    print("=== Game Analytics Dashboard ===\n")

    print("--- List Comprehension Examples ---")

    high_scorers = []
    for p in players:
        player_score = player_data[p]["score"]
        if player_score >= 2000:
            high_scorers.append(p)
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = []
    for s in scores:
        doubled = s * 2
        scores_doubled.append(doubled)
    print(f"Scores doubled: {scores_doubled}")

    active_players = []
    for p in players:
        player_level = player_data[p]["level"]
        if player_level >= 12:
            active_players.append(p)
    print(f"Active players: {active_players}\n")

    print("--- Dict Comprehension Examples ---")

    player_scores = {}
    for p in players:
        score = player_data[p]["score"]
        player_scores[p] = score
    print(f"Player scores: {player_scores}")

    high_score_players = []
    for p in players:
        if player_data[p]["score"] >= 2000:
            high_score_players.append(p)

    medium_score_players = []
    for p in players:
        score = player_data[p]["score"]
        if score >= 1800 and score < 2000:
            medium_score_players.append(p)

    low_score_players = []
    for p in players:
        if player_data[p]["score"] < 1800:
            low_score_players.append(p)

    score_categories = {
        "high": len(high_score_players),
        "medium": len(medium_score_players),
        "low": len(low_score_players),
    }
    print(f"Score categories: {score_categories}")

    counts = {}
    for p in players:
        achievements = player_data[p]["achievements"]
        counts[p] = achievements
    print(f"Achievement counts: {counts}\n")

    print("--- Set Comprehension Examples ---")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {player_data[p]["achievements"] for p in players}
    print(f"Unique achievments: {unique_achievements}")

    active_region = {
        "north"
        if player_data[p]["level"] >= 15
        else "south"
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
    print(f"Top performer: {top}")
