#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:05:51 by somenvie            #+#    #+#            #
#   Updated: 2026/02/25 02:14:51 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    card = EliteCard("Arcane Warrior", 6, "Legendary", 5, 4)

    print("EliteCard capabilities:")
    print(f"- Card: "
          f"{[m for m in dir(Card) if not m.startswith('_')]}")
    print(f"- Combatable: "
          f"{[m for m in dir(Combatable) if not m.startswith('_')]}")
    print(f"- Magical: "
          f"{[m for m in dir(Magical) if not m.startswith('_')]}")

    print(f"\nPlaying {card.name} (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
