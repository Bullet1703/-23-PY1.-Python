import csv
import json


INPUT_FILENAME = "input.cvs"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    json_data = []
    with open(INPUT_FILENAME, "r", newline="\n") as input_csv:
        reader = csv.DictReader(input_csv)
        for row in reader:
            json_data.append(row)


    with open(OUTPUT_FILENAME, "w") as output_json:
        json.dump(json_data, output_json, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")