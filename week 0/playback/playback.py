def main():
    user_input = input("").strip()
    print(replacing_space(user_input))


def replacing_space(sentence):
    out_put = sentence.replace(" ", "...")

    return out_put



if __name__=="__main__":
    main()