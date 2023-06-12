import argparse

parser = argparse.ArgumentParser(description="Data Converter")
parser.add_argument("input_file", help="Input file path")
parser.add_argument("output_file", help="Output file path")
args = parser.parse_args()

input_file_path = args.input_file
output_file_path = args.output_file
