import sys

import csv

def main():
    name_file = checker()
    try:
       final_no = count_lines(name_file)

    except FileNotFoundError:
       sys.exit("File does not exist")

    else:
       print(f"number of files lines is {final_no}")

        
        

def checker():
    user_input = sys.argv
    if len(user_input) <2:
        sys.exit("too few arguments")
    elif len(user_input)> 2:
        sys.exit("to many arguments")
   
    elif  not user_input[1].endswith(".py"):
        sys.exit("Not a Python file")   
    else:
        return user_input[1]
    


def count_lines(file):
    no_lines = 0
    with open(file, "r") as f:
        for row in f:
            line_strip = row.strip()

            if   line_strip.startswith("#"):
                continue

            if line_strip == "":
                continue
            else:
                no_lines +=1
    return no_lines


if __name__ == "__main__":
    main()