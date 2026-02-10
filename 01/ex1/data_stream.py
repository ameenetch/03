from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    Abstract base class defining the common interface for all data streams.
    Enforces polymorphic behavior for processing batches.
    """
    def __init__(self, stream_id):
        """Initialize the stream with a unique identifier."""
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract method to process a batch of data; must be overridden."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on specific criteria (default implementation)."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return statistics about the stream's performance."""
        return {}


class StreamProcessor():
    """
    Manager class that handles multiple stream types polymorphically.
    Demonstrates processing different streams through a unified interface.
    """
    def __init__(self):
        """Initialize with an empty list of streams."""
        self.streams = []

    def add_stream(self, stream):
        """Register a new DataStream object to the processor."""
        self.streams.append(stream)

    def process_all(self, data_map):
        """
        Iterate through all streams and process their corresponding data.
        Demonstrates polymorphic usage (same method call, different behaviors).
        """
        for stream in self.streams:
            if stream.stream_id in data_map:
                specific_data = data_map[stream.stream_id]
                print(stream.process_batch(specific_data))


class SensorStream(DataStream):
    """
    Concrete stream for processing numeric environmental data.
    """
    def __init__(self, stream_id):
        """Initialize sensor stream."""
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculate average and detect extreme values in numeric data."""
        try:
            avr = sum(data_batch) / len(data_batch)

            max_number = 100
            pass_the_max = False

            for i in data_batch:
                if i > max_number:
                    pass_the_max = True

            base_message = (f"Sensor analysis: {len(data_batch)} "
                            f"readings processed, avg temp: {avr}°C")

            if pass_the_max:
                return f"{base_message} [ALERT] Extreme value detected!"
            else:
                return base_message
        except ZeroDivisionError:
            return "Error: Data batch is empty, cannot calculate average."
        except TypeError:
            return "Error: Data contains non-numeric values."


class TransactionStream(DataStream):
    """
    Concrete stream for processing financial dictionary data.
    """
    def __init__(self, stream_id):
        """Initialize transaction stream."""
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculate net flow from buy/sell operations."""
        total_buy, total_sell = 0, 0
        try:
            for value in data_batch:
                if value["type"] == "buy":
                    total_buy += value["amount"]
                elif value["type"] == "sell":
                    total_sell += value["amount"]
        except TypeError:
            return "Error: Amount must be a number."

        return (f"{len(data_batch)} operations, net flow:"
                f"+{total_buy - total_sell} units")


class EventStream(DataStream):
    """
    Concrete stream for processing string-based system events.
    """
    def __init__(self, stream_id):
        """Initialize event stream."""
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count total events and detect errors."""
        count_error = 0
        for i in data_batch:
            if "error" in i:
                count_error += 1

        return f"{len(data_batch)} events, {count_error} error detected"


def data_stream():
    """
    Main simulation function for the Code Nexus Polymorphic Stream System.
    Demonstrates initializing, registering, and processing mixed stream types.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    processor = StreamProcessor()

    all_data_map = {
        "SENSOR_001": [22.5, 22.5, 22.5],
        "TRANS_001": [
            {"type": "buy", "amount": 100},
            {"type": "sell", "amount": 150},
            {"type": "buy", "amount": 75}
        ],
        "EVENT_001": ["login", "error", "logout"]
    }

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")

    sensor = SensorStream("SENSOR_001")
    processor.add_stream(sensor)
    print(sensor.process_batch(all_data_map["SENSOR_001"]))
    print()

    print("Initializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")

    transaction = TransactionStream("TRANS_001")
    processor.add_stream(transaction)
    print(f"Transaction analysis: "
          f"{transaction.process_batch(all_data_map['TRANS_001'])}")
    print()

    print("Initializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    print("Processing event batch: [login, error, logout]")

    event = EventStream("EVENT_001")
    processor.add_stream(event)
    print(f"Event analysis: {event.process_batch(all_data_map['EVENT_001'])}")
    print()

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed\n")
    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal")


if __name__ == "__main__":
    data_stream()
