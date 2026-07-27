import csv 

import sys

def main():
    old, new = check_input(sys.argv)
    split_write(old, new)


def check_files(files):
    if len(files) <3:
        sys.exit("too few command-line arguments")
    elif len(files) > 3:
        sys.exit("too many command-line arguments")

    old, new = files[1], files[2]
    if old.endswith(".csv") and new.endswith(".csv"):
        pass
    else:
        sys.exit("it isn't a csv file")

    return old, new


def split_write(old, new):
    with open(old, "r") as file:
        reader = csv.DictReader(file)

        with open(new, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames= ["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})



if __name__=="__main__":
    main()
