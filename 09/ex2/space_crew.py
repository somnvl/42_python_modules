#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   space_crew.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 19:02:21 by somenvie            #+#    #+#            #
#   Updated: 2026/02/26 02:49:36 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Pydantic models and validation for space crew management."""

from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    """Enumeration of crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Validated model representing a space mission crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Validated model representing a space mission with its crew."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        """Enforce safety and operational rules for space missions."""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        ranks = {m.rank for m in self.crew}
        if Rank.captain not in ranks and Rank.commander not in ranks:
            error = "Mission must have at least one Commander or Captain"
            raise ValueError(error)

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        return self


def main() -> None:
    """Demonstrate valid and invalid SpaceMission instantiation."""
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        sarah = CrewMember(
            member_id="sarah",
            name="Sarah Connor",
            rank="commander",
            age=36,
            specialization="Mission Command",
            years_experience=8,
        )
        john = CrewMember(
            member_id="john",
            name="John Smith",
            rank="lieutenant",
            age=47,
            specialization="Navigation",
            years_experience=16,
        )
        alice = CrewMember(
            member_id="alice",
            name="Alice Johnson",
            rank="officer",
            age=28,
            specialization="Engineering",
            years_experience=2,
        )

        crew1 = [sarah, john, alice]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2074-06-15T09:00:00",
            duration_days=900,
            crew=crew1,
            budget_millions=2500,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(crew1)}")
        print("Crew members:")
        for member in crew1:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")

    except ValidationError as e:
        print("Expected validation error:")
        print(str(e.errors()[0]["ctx"]["error"]))

    print()
    print("=" * 40)

    try:
        crew2 = [john, alice]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2074-06-15T09:00:00",
            duration_days=900,
            crew=crew2,
            budget_millions=2500,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(str(e.errors()[0]["ctx"]["error"]))


if __name__ == "__main__":
    main()

# python3 -m venv venv
# source venv/bin/activate
# pip install pydantic
