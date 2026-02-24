#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   advanced.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 15:25:52 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 15:30:44 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (
        f"Philosopher's stone created using {lead_to_gold()}"
        f" and {healing_potion()}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
