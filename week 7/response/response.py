from validator_collection import checkers

def main():
    email_input = input("What's your email address? ")
    print(check_email(email_input))


def check_email(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__=="__main__":
    main()

