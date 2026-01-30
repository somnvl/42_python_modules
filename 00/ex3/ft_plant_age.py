# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:26:22 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 03:14:28 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age < 0:
        print("\033[1;5;31;mInvalid value\033[0m")
    elif age > 60:
        print("\033[1;5;31;mPlant is ready to harvest!\033[0m")
    else:
        print("\033[1;5;31;mPlant needs more time to grow.\033[0m")
