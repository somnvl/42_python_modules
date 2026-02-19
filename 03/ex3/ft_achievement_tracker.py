#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:25 by somenvie            #+#    #+#            #
#   Updated: 2026/02/19 13:00:58 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Achievement Hunter - Exercise 3
Track unique achievements with sets
"""

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = set({"first_kill", "level_10", "treasure_hunter", "speed_demon"})
    bob = set({"first_kill", "level_10", "boss_slayer", "collector"})
    charlie = set({
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    })

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}\n")

    alice_only = alice.difference(bob).difference(charlie)
    bob_only = bob.difference(alice).difference(charlie)
    charlie_only = charlie.difference(alice).difference(bob)
    rare = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare}\n")

    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
