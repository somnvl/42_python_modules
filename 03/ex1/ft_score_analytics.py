#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:12 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 16:50:37 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Score Cruncher - Exercise 1
Analyzes player scores using lists
"""

from sys import argv

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    argc = len(argv)

    if argc == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ..."
        )
    else:
        scores = []

        try:
            x = 1
            while x < argc:
                scores.append(int(argv[x]))
                x += 1

            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")

        except ValueError:
            print("Error: All arguments must be valid integers")
