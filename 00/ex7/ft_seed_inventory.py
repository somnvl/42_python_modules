# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 01:41:14 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:12:58 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_seed_inventory(seed_type: str, quantity: int, unint: str) -> None:
    seed_type = str.capitalize(seed_type)
    if unint == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unint == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unint == "area":
        print(f"{seed_type} seeds: {quantity} square meters")
    else:
        print("\033[1;5;31;mUnkown unit type")
