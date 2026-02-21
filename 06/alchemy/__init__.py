#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 21:31:07 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 21:40:10 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .elements import create_fire, create_water

__version__ = "1.0.0"
__author__ = "Master Pythonicus"
__all__ = ["create_fire", "create_water"]
