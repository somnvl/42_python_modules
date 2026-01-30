# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:40:42 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:31:50 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def recursive(x, days):
    print("Day", x)
    if x < days:
        recursive(x + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if days <= 0:
        print("Invalid value")
        return
    x = 1
    recursive(x, days)
    print("Harvest time!")
