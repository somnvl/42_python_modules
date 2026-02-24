#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 17:45:32 by somenvie            #+#    #+#            #
#   Updated: 2026/02/24 15:05:21 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state = {"turn": 1, "player_mana": 6}
    print(f"Play result: {dragon.play(game_state)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    result = dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
