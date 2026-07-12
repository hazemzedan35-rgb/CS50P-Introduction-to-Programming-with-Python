import emoji

user_input = input("input: ")
result = emoji.emojize(user_input, language='alias')

print(f"Output: {result}")