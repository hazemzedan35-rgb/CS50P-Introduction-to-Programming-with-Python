import random
while True:

    try:    
        level = int(input("Level: "))
        if level != 0 and level > 0:
            continue
    except ValueError:
        level = int(input("Level: "))

