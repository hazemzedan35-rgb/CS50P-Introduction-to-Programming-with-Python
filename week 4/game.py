import random
while True:

    try:    
        level = int(input("Level: "))

        if level == 0  or level < 0:
            continue

        x = random.randint(1, level)
        break

    except ValueError:
        continue
    
while True:

   try:     
        guess = int(input("Guess: "))
        
        if guess < 0 or guess == 0:
            continue


        if x < guess:
            print("Too large!")
            continue

        elif x > guess:
            print("Too small!")
            continue

        print("Just right!")
        break
   
   except ValueError:
        continue

        
    
    
        



