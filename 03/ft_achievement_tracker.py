#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:25 by somenvie            #+#    #+#            #
#   Updated: 2026/02/11 03:39:26 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Achievement Hunter - Exercise 3: Track unique achievements with sets"""

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    # Alice achievements
    alice = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    # Bob achievements
    bob = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }
    # Charlie achievements
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===\n")

    # 1. All unique achievements (UNION)
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    # 2. Achievements common to ALL players (INTERSECTION)
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}\n")

    # 3. Rare achievements (owned by only 1 player)
    # Alice's unique achievements
    alice_only = alice.difference(bob).difference(charlie)
    # Bob's unique achievements
    bob_only = bob.difference(alice).difference(charlie)
    # Charlie's unique achievements
    charlie_only = charlie.difference(alice).difference(bob)
    rare = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare}\n")

    # 4. Alice vs Bob comparison
    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
