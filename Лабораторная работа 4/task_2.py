import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json(csv_filename, json_filename):
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)

    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)


if __name__ == '__main__':
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
