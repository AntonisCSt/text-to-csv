"""Supportive functions for main functionality."""

import os

def validate_file_path(file_path: str) -> bool:
    """
    Validate if the given file path exists and is a file.

    Args:
        file_path: Path to the file.

    Returns:
        True if file exists, False otherwise.
    """
    return os.path.isfile(file_path)
