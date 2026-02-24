#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   basic.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 15:25:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 15:28:32 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {create_earth()}"
