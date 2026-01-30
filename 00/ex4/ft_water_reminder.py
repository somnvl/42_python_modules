# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:32:35 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:32:09 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("\033[1;5;31;mWater the plants!")
    else:
        print("\033[1;5;31;mPlants are fine")
