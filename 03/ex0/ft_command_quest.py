#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:38:59 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 16:51:03 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Command Quest - Exercise 0
Demonstrates command-line argument handling with sys.argv
"""

from sys import argv

if __name__ == "__main__":
    print("=== Command Quest ===")

    argc = len(argv)

    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argc - 1}")
        x = 1
        while x < argc:
            print(f"Argument {x}: {argv[x]}")
            x += 1
    print(f"Total arguments: {argc}")
