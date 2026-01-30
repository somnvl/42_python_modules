# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 00:17:48 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:24:45 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    if day1 < 0:
        print("\033[1;5;31;mInvalid value")
        return
    day2 = int(input("Day 2 harvest: "))
    if day2 < 0:
        print("\033[1;5;31;mInvalid value")
        return
    day3 = int(input("Day 3 harvest: "))
    if day3 < 0:
        print("\033[1;5;31;mInvalid value")
        return
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
