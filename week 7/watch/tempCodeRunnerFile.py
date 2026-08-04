import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = s["iframe"]["src"]
    if url == "":
        return None
    elif matches := re.search(r"^(https?://)(youtube\.com|www\.youtube\.com){1}/(\w+)(/\w+)", url):
        converted_url = f"{matches.group(1)}youtu.be{matches.group(4)}"
        return converted_url





...


if __name__ == "__main__":
    main()