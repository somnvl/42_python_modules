#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   alien_contact.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 19:02:22 by somenvie            #+#    #+#            #
#   Updated: 2026/02/27 16:37:44 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Pydantic model and validation for alien contact reports."""

from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    """Enumeration of possible alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Validated model representing an alien contact report."""

    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_id: str = Field(min_length=5, max_length=15)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        """Enforce cross-field business rules for alien contact reports."""
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                error = "Telepathic contact requires at least 3 witnesses"
                raise ValueError(error)

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")

        return self


def main() -> None:
    """Demonstrate valid and invalid AlienContact instantiation."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-03-15T14:30:00",
            contact_type="radio",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        print("Expected validation error:")
        print(str(e.errors()[0]["ctx"]["error"]))

    print()
    print("=" * 40)

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-03-15T14:30:00",
            contact_type="telepathic",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(str(e.errors()[0]["ctx"]["error"]))


if __name__ == "__main__":
    main()

# python3 -m venv venv
# source venv/bin/activate
# pip install pydantic
