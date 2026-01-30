# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/01/29 20:38:42 by somenvie            #+#    #+#            #
#   Updated: 2026/01/30 02:24:21 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_plot_area():
    length = int(input("Enter length: "))
    if length <= 0:
        print("\033[1;5;31;mInvalid length")
        return
    width = int(input("Enter width: "))
    if width <= 0:
        print("\033[1;5;31;mInvalid width")
        return
    area = length * width
    print(f"Plot area: {area}")
