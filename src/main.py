"""Core logic for TXT to CSV conversion."""
from src.utils.txt_utils import convert_txt_to_csv
from src.config import Config
from src.validate_file import validate_file_path

def main() -> None:
    """
    Main function to execute the TXT to CSV conversion.

    Users can specify input file, output file, and the delimiter.
    """
    input_file = input("Enter the path of the TXT file: ")
    output_file = input("Enter the path for the output CSV file: ")
    separator = input(f"Enter the separator (default is {Config.DEFAULT_SEPARATOR}): ") or Config.DEFAULT_SEPARATOR

    if validate_file_path(input_file):
        convert_txt_to_csv(input_file, output_file, separator)
        print(f"File converted successfully and saved to {output_file}.")
    else:
        print("Invalid file path. Please try again.")


if __name__ == "__main__":
    main()
