user_input = input("enter your text: ").strip()
vowels = "ioeua"

for i in user_input:
    if i.lower() not in vowels:
            print(i, end=(""))
    else:
          print("", end=(""))