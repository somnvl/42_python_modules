#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 16:08:23 by somenvie            #+#    #+#            #
#   Updated: 2026/02/17 16:09:54 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Stream Wizard - Exercise 5
Process data streams with generators
"""

import time


def game_event_stream(count: int):
    """Generate game events one by one (streaming)"""
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        seed = int(time.time() * 1000000 + i) % 1000

        player_idx = ((i * 7) + (seed * 3)) % len(players)
        event_idx = ((i * 11) + (seed * 5)) % len(events)
        level = ((i * 13) + (seed * 7)) % 20 + 1

        yield {
            "id": i,
            "player": players[player_idx],
            "level": level,
            "event": events[event_idx],
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


def print_sequence(generator, name: str):
    """Print a sequence from a generator with proper formatting"""
    print(f"{name}: ", end="")
    iterator = iter(generator)

    first_value = next(iterator)
    print(first_value, end="")

    for value in iterator:
        print(f", {value}", end="")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    start_time = time.time()

    i = 1
    for event in game_event_stream(event_count):
        if i <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['event']}"
            )
        elif i == 4:
            print("...\n")

        if event["level"] >= 10:
            high_level_count += 1
        if event["event"] == "found treasure":
            treasure_count += 1
        if event["event"] == "leveled up":
            levelup_count += 1

        i += 1

    end_time = time.time()
    processing_time = end_time - start_time

    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.4f} seconds\n")

    print("=== Generator Demonstration ===")
    print_sequence(fibonacci_generator(10), "Fibonacci sequence (first 10)")
    print()
    print_sequence(prime_generator(5), "Prime numbers (first 5)")
