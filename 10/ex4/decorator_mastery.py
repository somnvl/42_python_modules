#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 03:06:03 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 04:21:32 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import time
import functools
from typing import Any


def spell_timer(func: callable) -> callable:
    """Measure and print execution time of the decorated function."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrap func with timing logic."""
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """Return decorator that checks first arg is >= min_power."""

    def decorator(func: callable) -> callable:
        """Decorate func with power validation."""

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrap func with power check."""
            power = args[1] if len(args) > 1 else args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Return decorator that retries func up to max_attempts on failure."""

    def decorator(func: callable) -> callable:
        """Decorate func with retry logic."""

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrap func with retry on exception."""
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Guild managing mages and spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is 3+ chars and letters/spaces only."""
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Cast a spell if power is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball() -> str:
        """Simulate a fireball spell."""
        time.sleep(0.1)
        return "Fireball cast!"

    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))
