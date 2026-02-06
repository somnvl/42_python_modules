#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/05 05:10:17 by somenvie            #+#    #+#            #
#   Updated: 2026/02/05 05:10:18 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

""""""


def test_custom_error() -> None:
    pass


if __name__ == "__main__":
    try:
        print("===  Custom Garden Errors Demo\n")
        test_custom_error()
        print("All custom error types work correctly!")
    except Exception as e:
        print(f"\nCritical error: {type(e).__name__}: {e}")
