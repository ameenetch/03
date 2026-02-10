from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class defining the common interface for data processors.
    Enforces a standard structure for validating and processing data.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if the provided data is valid for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        return result


class NumericProcessor(DataProcessor):
    """
    Concrete processor for handling numeric list data.
    """
    def process(self, data: Any) -> str:
        """Calculate statistics (sum, average) for a list of numbers."""
        try:
            if not data:
                return "Processed 0 numeric values, sum=0, avg=0.0"

            sum_numbers = 0
            total_len = len(data)

            for i in data:
                sum_numbers += i

            avr = sum_numbers / total_len
            return (f"Processed {total_len} numeric values, "
                    f"sum={sum_numbers}, avg={avr}")

        except ZeroDivisionError:
            return "Error: Data list is empty."

    def validate(self, data: Any) -> bool:
        """Validate that data is a list containing only integers or floats."""
        if not isinstance(data, list):
            return False

        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    """
    Concrete processor for handling text string data.
    """
    def process(self, data: Any) -> str:
        """Analyze text to count characters and words."""
        list_word = data.split()
        number_word = len(list_word)
        number_char = len(data)

        return f"Processed text: {number_char} characters, {number_word} words"

    def validate(self, data: Any) -> bool:
        """Validate that data is a string."""
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """
    Concrete processor for handling log entry strings.
    """
    def process(self, data: Any) -> str:
        """Format log messages based on their severity level"""
        parts = data.split(":", 1)
        level = parts[0]
        message = parts[1].strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        else:
            return f"[INFO] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a string containing a colon separator."""
        return isinstance(data, str) and ":" in data


def data_stream():
    """
    Main function to simulate the Data Processor Foundation.
    Demonstrates validation, processing, and polymorphic behavior.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    numbers_pro = NumericProcessor()

    if numbers_pro.validate(data):
        print("Validation: Numeric data verified")
        print(f"Output: {numbers_pro.process(data)}\n")

    string = "Hello Nexus World"
    str_pro = TextProcessor()

    print("Initializing Text Processor...")
    print(f'Processing data: "{string}"')

    if str_pro.validate(string):
        print("Validation: Text data verified")
        print(f"Output: {str_pro.process(string)}\n")

    print("Initializing Log Processor...")
    string_2 = "ERROR: Connection timeout"
    print(f"Processing data: {string_2}")

    error_pro = LogProcessor()
    if error_pro.validate(string_2):
        print("Validation: Log entry verified")
        print(f"Output: {error_pro.process(string_2)}\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print(f"Result 1: {numbers_pro.process(data)}")
    print(f"Result 2: {str_pro.process(string)}")
    print(f"Result 3: {error_pro.process(string_2)}\n")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
