"""Data models for the application."""

from pydantic import BaseModel


class FileConversionRequest(BaseModel):
    """
    Data model for a file conversion request.

    Attributes:
        input_path: Path to the input TXT file.
        output_path: Path to the output CSV file.
        separator: Separator for the CSV file.
    """

    input_path: str
    output_path: str
    separator: str
