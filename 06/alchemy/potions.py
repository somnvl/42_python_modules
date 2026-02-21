#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 23:01:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 23:13:40 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from . import elements


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {create_air()}"
        f" and {create_water()}"
    )


def wisdom_potion() -> str:
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    all_elements = f"{fire}, {water}, {earth}, {air}"
    return f"Wisdom potion brewed with all elements: {all_elements}"
