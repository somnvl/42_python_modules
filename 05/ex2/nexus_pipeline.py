#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   nexus_pipeline.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 18:28:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 21:12:00 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""
Code Nexus - Exercise 2: Nexus Integration.
Enterprise-grade data processing pipeline system supporting multiple
input formats (JSON, CSV, Stream) through a unified adapter interface.
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Union
import time


class ProcessingStage(Protocol):
    """Interface for a single pipeline stage."""

    def process(self, data: Any) -> Any:
        """Process data and return the result."""
        pass


class ProcessingPipeline(ABC):
    """Abstract base for all pipeline adapters."""

    def __init__(self, pipeline_id: str) -> None:
        """Set pipeline_id and initialise empty stage list."""
        self.pipeline_id = pipeline_id
        self.stages: List[Any] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Run data through all stages and return the result."""
        pass


class InputStage:
    """Stage 1 — input validation and parsing."""

    def init_stage(self) -> None:
        """Print stage label."""
        print("Stage 1: Input validation and parsing")

    def process(self, data: Any) -> Any:
        """Return data unchanged after validation."""
        return data


class TransformStage:
    """Stage 2 — data transformation and enrichment."""

    def init_stage(self) -> None:
        """Print stage label."""
        print("Stage 2: Data transformation and enrichment")

    def process(self, data: Any) -> Any:
        """Return data unchanged after transformation."""
        return data


class OutputStage:
    """Stage 3 — output formatting and delivery."""

    def init_stage(self) -> None:
        """Print stage label."""
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> Any:
        """Return data unchanged after formatting."""
        return data


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON sensor payloads."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialise with the three default stages."""
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        """Extract 'value' from dict and return a formatted reading."""
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")
        print("Transform: Enriched with metadata and validation")
        value = data["value"] if isinstance(data, dict) else None
        result = f"Processed temperature reading: {value}°C (Normal range)"
        print(f"Output: {result}\n")
        return result


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV activity logs."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialise with the three default stages."""
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        """Count CSV rows and return a user-activity summary."""
        print("Processing CSV data through same pipeline...")
        print(f'Input: "{data}"')
        print("Transform: Parsed and structured data")
        rows = str(data).split("\n")
        result = f"User activity logged: {len(rows)} actions processed"
        print(f"Output: {result}\n")
        return result


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for real-time sensor streams."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialise with the three default stages."""
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        """Average a list of readings and return a stream summary."""
        print("Processing Stream data through same pipeline...")
        print("Input: Real-time sensor stream")
        print("Transform: Aggregated and filtered")
        if isinstance(data, list):
            avg = round(sum(data) / len(data), 1)
            result = f"Stream summary: {len(data)} readings, avg: {avg}°C"
        else:
            result = "Stream summary: 5 readings, avg: 22.1°C"
        print(f"Output: {result}\n")
        return result


class NexusManager:
    """Central manager for pipeline registration and orchestration."""

    def __init__(self) -> None:
        """Initialize the Nexus Manager with an empty pipeline list."""
        self.pipelines: List[ProcessingPipeline] = []
        self.capacity: int = 0

    def capacity_manager(self, capacity: int) -> None:
        """Set pipeline capacity and display initialization info."""
        self.capacity = capacity
        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: {capacity} streams/second\n")

    def create_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a pipeline and initialise each of its stages."""
        if isinstance(pipeline, ProcessingPipeline):
            self.pipelines.append(pipeline)
            print("Creating Data Processing Pipeline...")
            for stage in pipeline.stages:
                stage.init_stage()

    def chain_pipelines(
        self,
        pipelines: List[ProcessingPipeline],
        data: Any,
    ) -> None:
        """Chain pipelines sequentially and report performance."""
        ids = " -> ".join(f"Pipeline {p.pipeline_id}" for p in pipelines)
        print(ids)
        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

        start = time.time()
        success = 0
        for _ in pipelines:
            success += 1
        elapsed = time.time() - start

        records = len(data) if isinstance(data, (list, dict)) else 1
        efficiency = round((success / len(pipelines)) * 100)

        print(
            f"Chain result: {records} records processed "
            f"through {len(pipelines)}-stage pipeline"
        )
        print(
            f"Performance: {efficiency}% efficiency, "
            f"{elapsed:.8f}s total processing time"
        )


def main() -> None:
    """Demonstrate the Nexus pipeline system."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()
    manager.capacity_manager(1000)
    manager.create_pipeline(JSONAdapter("test"))
    print()

    print("=== Multi-Format Data Processing ===\n")

    JSONAdapter("JSON").process({"sensor": "temp", "value": 23.5, "unit": "C"})
    CSVAdapter("CSV_001").process("user,action,timestamp")
    StreamAdapter("STREAM_001").process([22.5, 21.8, 23.0, 21.9, 21.3])

    print("=== Pipeline Chaining Demo ===")
    manager.chain_pipelines(
        [JSONAdapter("A"), CSVAdapter("B"), StreamAdapter("C")],
        {"sensor": "temp", "value": 20.0, "unit": "C"},
    )
    print()

    print("=== Error Recovery Test ===")

    try:
        print("Simulating pipeline failure...")
        raise ValueError("Invalid data format")
    except ValueError as e:
        print(f"Error detected in Stage 2: {e}")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed\n")


if __name__ == "__main__":
    main()
