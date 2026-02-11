#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/05 05:09:58 by somenvie            #+#    #+#            #
#   Updated: 2026/02/05 05:10:02 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Agricultural data validation pipeline with exception handling."""


def check_temperature(temp_str: str) -> int | None:
    """Validates temperature string for plant range (0-40°C)."""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    """Tests temperature validation with various inputs."""
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
