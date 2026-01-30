# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 01:24:30 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:34:49 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_garden_summary():
    garden = input("Enter garden name: ")
    plants = int(input("Enter number of plants: "))
    print(f"Garden: {garden}")
    print(f"Plants: {plants}")
    print("Status: \033[1;5;31;mGrowing well!")
