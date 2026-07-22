import sys

def main():
    try:
        file_name = checker()

    except (IndexError, ValueError, FileNotFoundError) as error:
        sys.exit(error)
    else:
        number_of_lines = lines_counter(file_name)
        print(number_of_lines)

def checker():
    user_input = sys.argv

    if len(user_input) < 2:
        raise IndexError("too few arguments!!")
    elif len(user_input) > 2:
        raise IndexError("too many arguments!!")
    elif not user_input[1].endswith(".py"):
        raise ValueError("not python file")
    else:
        return user_input[1]




def lines_counter(file):
    with open(file, "r") as f:
        no_lines = 0
        for row in f:
            cleaned_row = row.strip()
            if cleaned_row.startswith("#"):
                continue
            elif cleaned_row == "":
                continue
            else:
                no_lines +=1
    return no_lines


if __name__ == "__main__":
    main()
