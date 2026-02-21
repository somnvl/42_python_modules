#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   stream_processor.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 19:32:04 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 18:24:54 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""
Code Nexus - Exercise 0: Data Processor Foundation.
Polymorphic data processing system using ABC and method overriding.
"""


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string with a standard prefix."""
        return f"Output: {result}\n"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric data (list, tuple or set)."""

    def process(self, data: Any) -> str:
        """Compute sum and average of numeric values."""
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        """Return True if data is a list, tuple or set."""
        if type(data) is list or tuple or set:
            return True
        return False


class TextProcessor(DataProcessor):
    """Processor specialized for plain text data."""

    def process(self, data: Any) -> str:
        """Count characters and words in the text."""
        words = data.split()
        return f"Processed text: {len(data)} characters, {len(words)} words"

    def validate(self, data: Any) -> bool:
        """Return True if data is a string."""
        if type(data) is str:
            return True
        return False


class LogProcessor(DataProcessor):
    """Processor specialized for log entries with severity levels."""

    def process(self, data: Any) -> str:
        """Parse log level and message, tag alerts for critical levels."""
        levels = ["ERROR", "INFO", "WARNING", "DEBUG", "CRITICAL"]
        alert_levels = ["ERROR", "CRITICAL", "WARNING"]

        level = "UNKNOWN"
        for lvl in levels:
            if lvl in data:
                level = lvl
                break

        message = data.split(":", 1)[1].strip()
        tag = "ALERT" if level in alert_levels else level

        return f"[{tag}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        """Return True if data is a string containing a known log level."""
        if type(data) is str:
            levels = ["ERROR", "INFO", "WARNING", "DEBUG", "CRITICAL"]
            for level in levels:
                if level in data:
                    return True
        return False


def main() -> None:
    """Run the polymorphic data processor demonstration."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric
    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    if numeric.validate(data_num):
        print("Validation: Numeric data verified")
    result = numeric.process(data_num)
    print(numeric.format_output(result))

    # Text
    print("Initializing Text Processor...")
    text = TextProcessor()
    data_txt = "Hello Nexus World"
    print(f'Processing data: "{data_txt}"')
    if text.validate(data_txt):
        print("Validation: Text data verified")
    result = text.process(data_txt)
    print(text.format_output(result))

    # Log
    print("Initializing Log Processor...")
    log = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f'Processing data: "{data_log}"')
    if log.validate(data_log):
        print("Validation: Log entry verified")
    result = log.process(data_log)
    print(log.format_output(result))

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    proc1 = NumericProcessor()
    proc2 = TextProcessor()
    proc3 = LogProcessor()

    print(f"Result 1: {proc1.process([1, 2, 3])}")
    print(f"Result 2: {proc2.process('Hello World')}")
    print(f"Result 3: {proc3.process('INFO: System ready')}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
