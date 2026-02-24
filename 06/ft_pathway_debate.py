#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_pathway_debate.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 15:26:00 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 15:51:23 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    ltd = alchemy.transmutation.lead_to_gold()
    ps = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.lead_to_gold(): {ltd}")
    print(f"alchemy.transmutation.philosophers_stone(): {ps}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
