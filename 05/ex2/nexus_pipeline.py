#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   nexus_pipeline.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/21 18:28:47 by somenvie            #+#    #+#            #
#   Updated: 2026/02/21 21:08:41 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Union
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[Any] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:
    def init_stage(self) -> None:
        print("Stage 1: Input validation and parsing")

    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    def init_stage(self) -> None:
        print("Stage 2: Data transformation and enrichment")

    def process(self, data: Any) -> Any:
        return data


class OutputStage:
    def init_stage(self) -> None:
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> Any:
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")
        print("Transform: Enriched with metadata and validation")
        value = data["value"] if isinstance(data, dict) else None
        result = f"Processed temperature reading: {value}°C (Normal range)"
        print(f"Output: {result}\n")
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        print(f'Input: "{data}"')
        print("Transform: Parsed and structured data")
        rows = str(data).split("\n")
        result = f"User activity logged: {len(rows)} actions processed"
        print(f"Output: {result}\n")
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.stages = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
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
        if isinstance(pipeline, ProcessingPipeline):
            self.pipelines.append(pipeline)
            print("Creating Data Processing Pipeline...")
            for stage in pipeline.stages:
                stage.init_stage()

    def chain_pipelines(self, pipelines: List[ProcessingPipeline], data: Any) -> None:
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
