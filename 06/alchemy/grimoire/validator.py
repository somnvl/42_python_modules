#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   validator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 16:13:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 16:15:16 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

VALID_ELEMENTS = ["fire", "water", "earth", "air"]


def validate_ingredients(ingredients: str) -> str:
    if any(element in ingredients for element in VALID_ELEMENTS):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
