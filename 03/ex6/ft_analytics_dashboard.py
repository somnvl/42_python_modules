#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 16:25:03 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 16:26:30 by somenvie           ###   ########.fr      #
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

    high_scorers = [p for p in players if player_data[p]["score"] >= 2000]
    print(f"High scorers (2000+): {high_scorers}")

    scores_doubled = [s * 2 for s in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p for p in players if player_data[p]["level"] >= 12]
    print(f"Active players (level 12+): {active_players}\n")

    print("--- Dict Comprehension Examples ---")

    player_scores = {p: player_data[p]["score"] for p in players}
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

    counts = {p: player_data[p]["achievements"] for p in players}
    print(f"Achievement counts: {counts}\n")

    print("--- Set Comprehension Examples ---")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    high_performers = set()
    for p in players:
        score = player_data[p]["score"]
        achievements = player_data[p]["achievements"]
        if score > 2000 and achievements > 5:
            high_performers.add(p)
    print(f"High performers: {high_performers}")

    levels = {player_data[p]["level"] for p in players}
    sorted_levels = sorted(levels)
    print(f"Unique levels: {sorted_levels}\n")

    print("--- Combined Analysis ---")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_score = sum(scores)
    count = len(scores)
    average = total_score / count
    print(f"Average score: {average:.1f}")

    top = max(players, key=lambda p: player_data[p]["score"])
    top_score = player_data[top]["score"]
    top_ach = player_data[top]["achievements"]

    print(f"Top performer: {top}")
    print(f"Score: {top_score} points")
    print(f"Achievements: {top_ach}")
