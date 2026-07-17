def main():
    user_input = input("enter your text: ").strip()

    print(shorten(user_input))


def shorten(word):
    vowels = "ioeua"
    result = ""

    for i in word:
      if i.lower() not in vowels:
        result +=i
    
    return result

if __name__ == "__main__":
    main()