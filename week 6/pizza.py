import sys

from tabulate import tabulate

import csv

def main():
    
    file_name = sys.argv
    if len(file_name) <2:
        sys.exit()
    elif len(file_name) > 2:
        sys.exit()


    
    checked_file = check_user_input(file_name[1])
    final_table = format_a_table(checked_file)

    print(final_table)


def check_user_input(thing):
    
    if  thing.endswith(".csv"):
        pass

    else: 
        sys.exit("it isn't a csv file")

    try:
        with open(thing, "r") as f:
            pass
    except FileNotFoundError:
        sys.exit("file isn't found")

    return thing
        




def format_a_table(file):
    with open(file, "r") as f:
        reader = csv.reader(f)

        return tabulate(reader, headers="firstrow", tablefmt="grid")



if __name__=="__main__":
    main()