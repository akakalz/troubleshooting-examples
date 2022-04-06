import csv


def main() -> None:
    csv_file = "./src/csv_error/example_file.txt"
    with open(csv_file, "r") as in_file:
        line_count = 0
        csv_reader = csv.reader(in_file, delimiter="|", quotechar='"')
        for line in csv_reader:
            line_count += 1
    print(line_count, "lines in file.")


if __name__ == "__main__":
    main()
