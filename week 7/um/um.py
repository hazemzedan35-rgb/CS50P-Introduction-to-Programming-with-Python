import re


def main():
    print(count(input("Text: ")))


def count(s):
    number_word = re.findall(r"\bum\b", s , re.IGNORECASE)

    return len(number_word)


if __name__ == "__main__":
    main()