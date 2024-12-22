"""Utility functions for file conversion."""

import csv
from typing import Union


def convert_txt_to_csv(input_path: str, output_path: str, separator: str) -> None:
    """
    Convert a TXT file to a CSV file with a specified separator.

    Args:
        input_path: Path to the input TXT file.
        output_path: Path to the output CSV file.
        separator: Separator to use in the CSV file.

    Raises:
        ValueError: If the input file cannot be read or written to.
    """
    try:
        with open(input_path, "r") as txt_file, open(output_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=separator)
            for line in txt_file:
                writer.writerow(line.strip().split())
    except Exception as e:
        raise ValueError(f"Error processing file: {e}")
