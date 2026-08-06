def main():
    user_input = input("Enter: ")
    print(convert(user_input))

def convert(text):
    out_put = text.replace(":)", "🙂").replace(":(", "🙁")

    return out_put


if __name__=="__main__":
    main()