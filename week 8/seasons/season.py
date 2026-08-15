from datetime import date

import re, sys, inflect

def main():
    entered_date = check_valid_input(get_date())
    whole_minutes = minutes_converter(*entered_date)
    print(convert_number_to_letters(whole_minutes))


def get_date():
    date_of_birth = input("Date of Birth: ")
    return date_of_birth


def check_valid_input(date):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", date):
        year, month, day = match.groups()
        return int(year), int(month), int(day)
    else:
        sys.exit("invalid date")


def minutes_converter(year, month, day):
    today = date.today()
    birth_date = date(year, month, day)
    diff = today - birth_date
    total_days = diff.days
    total_minutes = total_days * 24 * 60

    return total_minutes


def convert_number_to_letters(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()

    return f'{words} minutes'



if __name__ == "__main__":
    main()
