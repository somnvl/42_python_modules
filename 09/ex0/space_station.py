#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   space_station.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 19:02:24 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 15:32:59 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Pydantic model and validation demonstration for space station data."""

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """Validated model representing a space station and its statistics."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """Demonstrate valid and invalid SpaceStation instantiation."""
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Offline"
        print(f"Status: {status}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    print()
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()

# python3 -m venv venv
# source venv/bin/activate
# pip install pydantic
