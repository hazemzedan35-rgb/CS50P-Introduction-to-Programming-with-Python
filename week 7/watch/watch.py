import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s == "":
        return None
    
    elif matches := re.search(r'src="https?://(?:www\.)?youtube\.com{1}/embed/([a-zA-Z0-9_-]+)"', s):
        converted_url = f"https://youtu.be/{matches.group(1)}"
        return converted_url
    else:
        return None


if __name__ == "__main__":
    main()
