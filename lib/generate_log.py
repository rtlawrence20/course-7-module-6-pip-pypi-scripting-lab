from datetime import datetime
import sys
from typing import List, Any


def generate_log(data: List[Any]):
    """
    Generate a log file named 'log_YYYYMMDD.txt' and write one entry per line.
    Args:
        data (list): List of entries to write.
    Returns:
        str: The generated filename.
    Raises:
        ValueError: If data is not a list.
    """
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log file '{filename}' generated successfully.")
    return filename


def _parse_cli_args(argv: List[str]) -> List[str]:
    """
    CLI behavior:
      - If args provided, each arg is one log entry.
      - If no args, read lines from stdin until EOF.
    """
    if argv:
        return argv
    return [line.rstrip("\n") for line in sys.stdin]


def main() -> None:
    """
    CLI entry point for log generation.
    Collects entries from command-line arguments or stdin and generates the log file.
    """
    entries = _parse_cli_args(sys.argv[1:])
    generate_log(entries)


if __name__ == "__main__":
    main()
