#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 03:06:03 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 03:47:06 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Lambda spells: anonymous function mastery using map, filter, sorted."""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level in descending order."""
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages with power >= min_power."""
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name with '* ' prefix and ' *' suffix."""
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return max, min and average power levels of a mage list."""
    powers = list(map(lambda x: x["power"], mages))
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": round(sum(powers) / len(mages), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]
    sorted_art = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    print(
        f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power)"
        f" comes before"
        f" {sorted_art[1]['name']} ({sorted_art[1]['power']} power)"
    )

    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print("\nTesting spell transformer...")
    print(" ".join(transformed))
