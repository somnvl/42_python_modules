#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 03:39:36 by somenvie            #+#    #+#            #
#   Updated: 2026/02/16 18:31:31 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Stream Wizard - Exercise 5
Process data streams with generator
"""


def game_event_stream(count: int):
    """
    Generate game events one by one (streaming)
    """
    import random

    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        yield {
            "id": i,
            "player": random.choice(players),
            "level": random.randint(1, 20),
            "event": random.choice(events),
        }


def fibonacci_generator(limit: int):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def prime_generator(limit: int):
    """Generate prime numbers up to limit"""
    count = 0
    num = 2
    while count < limit:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    # Process 1000 events (streaming!)
    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    # Statistics counters
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    # Process events one by one (for-in loop)
    for i, event in enumerate(game_event_stream(event_count), 1):
        # Show first 3 events
        if i <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['event']}"
            )
        elif i == 4:
            print("...\n")

        # Count statistics (without storing all events!)
        if event["level"] >= 10:
            high_level_count += 1
        if event["event"] == "found treasure":
            treasure_count += 1
        if event["event"] == "leveled up":
            levelup_count += 1

    # Display analytics
    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)\n")

    # Fibonacci demonstration
    print("=== Generator Demonstration ===")
    fib = fibonacci_generator(10)
    fib_list = list(fib)  # Convert generator to list
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_list))}")

    # Prime numbers demonstration
    primes = prime_generator(5)
    prime_list = list(primes)
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_list))}")
