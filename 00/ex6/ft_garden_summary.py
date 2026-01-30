# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/30 01:24:30 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 03:04:53 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_garden_summary():
    garden = input("Enter garden name: ")
    plants = int(input("Enter number of plants: "))
    print(f"Garden: {garden}")
    print(f"Plants: {plants}")
    if plants < 0:
        print("\033[1;5;31;mInvalid value\033[0m")
        return
    elif plants == 0:
        print("Status: \033[1;5;31;mNo plants!\033[0m")
    else:
        print("Status: \033[1;5;31;mGrowing well!\033[0m")
