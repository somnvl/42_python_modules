# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:32:35 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 03:16:36 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days < 0:
        print("\033[1;5;31;mInvalid value\033[0m")
    elif days > 2:
        print("\033[1;5;31;mWater the plants!\033[0m")
    else:
        print("\033[1;5;31;mPlants are fine\033[0m")
