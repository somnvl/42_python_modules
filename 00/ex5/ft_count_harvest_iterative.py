# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:41:12 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:51:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_count_harvest_iterative():
    days = int(input("Days until harvest: ")) + 1
    if days == 0:
        print("Harvest time!")
        return
    elif days < 0:
        print("Invalid value")
        return
    for x in range(1, days, 1):
        print("Day", x)
    print("Harvest time!")
