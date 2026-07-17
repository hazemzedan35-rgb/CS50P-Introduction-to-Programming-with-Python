def main():
    user_greating = input("Enter a greeting: ").strip().lower()
    print(value(user_greating))


def value(greeting):
    if greeting.lower().startswith("hello"):
        return "$0"
    elif greeting.lower().startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()


