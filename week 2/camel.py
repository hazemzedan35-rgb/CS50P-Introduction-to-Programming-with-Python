camelCase = input("what is your variable name? ").strip()
snake = []

for i in camelCase:
    if i.isupper():
        snake.append("_")
        snake.append(i.lower())
    else:
        snake.append(i)
        
result = "".join(snake)
print(result)
