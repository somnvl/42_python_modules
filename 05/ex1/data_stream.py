#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 16:23:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 18:26:19 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


"""
Code Nexus - Exercise 1: Polymorphic Streams.
Advanced data streaming system using ABC, method overriding and isinstance.
"""


from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    """Abstract base class defining the core streaming interface."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the stream with a unique identifier."""
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return an analysis string."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter string items in the batch matching the given criteria."""
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria in item
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {"type": "Unknown"}


class SensorStream(DataStream):
    """Stream specialized for environmental sensor readings."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the sensor stream with its identifier."""
        super().__init__(stream_id)
        self.name = "Sensor Stream"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Compute the number of readings and average temperature."""
        nb = len(data_batch)
        temps = [float(d.split(":")[1]) for d in data_batch if "temp" in d]
        avg = sum(temps) / len(temps) if temps else 0
        return f"Sensor analysis: {nb} readings processed, avg temp: {avg}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics."""
        return {"type": "Environmental Data"}


class TransactionStream(DataStream):
    """Stream specialized for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the transaction stream with its identifier."""
        super().__init__(stream_id)
        self.name = "Transaction Stream"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Compute total operations and net financial flow."""
        nb = len(data_batch)
        net = 0
        for item in data_batch:
            op, amount = str(item).split(":")
            if op == "buy":
                net += int(amount)
            else:
                net -= int(amount)
        sign = "+" if net >= 0 else ""
        return (f"Transaction analysis: {nb} operations, "
                f"net flow: {sign}{net} units")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics."""
        return {"type": "Financial Data"}


class EventStream(DataStream):
    """Stream specialized for system event data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the event stream with its identifier."""
        super().__init__(stream_id)
        self.name = "Event Stream"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count total events and detected errors in the batch."""
        nb = len(data_batch)
        errors = len([e for e in data_batch if "error" in str(e)])
        return f"Event analysis: {nb} events, {errors} error detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics."""
        return {"type": "System Events"}


class StreamProcessor:
    """Handles any DataStream type polymorphically."""

    @staticmethod
    def process_stream(stream: DataStream, batch: List[Any]) -> str:
        """Process a batch through the given stream with error handling."""
        if not isinstance(stream, DataStream):
            return "Error: Invalid stream type"
        try:
            return stream.process_batch(batch)
        except (TypeError, ValueError) as e:
            return f"Error: {e}"


def main() -> None:
    """Run the polymorphic stream processing demonstration."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    streams = [
        (
            SensorStream("SENSOR_001"),
            ["temp:22.5", "humidity:65", "pressure:1013"]
        ),
        (
            TransactionStream("TRANS_001"),
            ["buy:100", "sell:150", "buy:75"]
        ),
        (
            EventStream("EVENT_001"),
            ["login", "error", "logout"]
        ),
    ]

    for stream, data in streams:
        print(f"Initializing {stream.name}...")
        stats = stream.get_stats()
        print(f"Stream ID: {stream.stream_id}, Type: {stats['type']}")
        print(f"Processing batch: {data}")
        print(StreamProcessor.process_stream(stream, data))
        print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    batch = [
        (
            SensorStream("SENSOR_001"),
            ["temp:22.5", "humidity:65"],
            "Sensor data",
            "readings",
        ),
        (
            TransactionStream("TRANS_001"),
            ["buy:100", "sell:150", "buy:75", "buy:200"],
            "Transaction data",
            "operations",
        ),
        (
            EventStream("EVENT_001"),
            ["login", "error", "logout"],
            "Event data",
            "events",
        ),
    ]

    print("Batch 1 Results:")
    for stream, data, label, unit in batch:
        print(f"- {label}: {len(data)} {unit} processed")

    print("\nStream filtering active: High-priority data only")
    sensor_data = ["temp:85", "temp:88", "humidity:65", "temp:22.5"]
    transaction_data = ["buy:1000", "sell:50", "buy:75", "sell:200"]

    sensor = SensorStream("SENSOR_002")
    transaction = TransactionStream("TRANS_002")

    critical = sensor.filter_data(sensor_data, "temp:8")
    large = transaction.filter_data(transaction_data, "000")

    print(
        f"Filtered results: {len(critical)} critical sensor alerts, "
        f"{len(large)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
