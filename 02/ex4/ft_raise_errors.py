#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_raise_errors.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/10 19:52:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/10 19:52:52 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def check_plant_health(plant_name = str, water_level: int, sunlight_hours: int) -> None:
    pass


def test_plant_checks() -> None:
    print("Testing good values...")
    check_plant_health()
    print("Testing empty plant name...")
    check_plant_health()
    print("Testing bad water level...")
    check_plant_health()
    print("Testing bad sunlight hours...")
    check_plant_health()


if __name__ == "__main__":
    print("===  Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
