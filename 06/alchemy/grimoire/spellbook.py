#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   spellbook.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 16:16:09 by somenvie            #+#    #+#            #
#   Updated: 2026/02/23 16:47:00 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
