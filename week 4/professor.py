import random


def main():
    score = 0 
    level = get_level()

    # creating a for loop for asking 10 questions.
    for i in range(0,10):
        x = generate_integer(level)
        y = generate_integer(level)

        correct_answer = x + y
        user_answer = int(input(f"{x} + {y} = "))

        # if the user answers the question right he will get one point and start the new question from the main 10 questions. 
        if user_answer == correct_answer:
            score += 1
            continue

        # if the user answers the question wrong he will get "EEE" message and start a small loop count another two chances for this question.       
        else:

            print("EEE")   
            for n in range(0,2):
                user_answer = int(input(f"{x} + {y} = "))

                # if the user answers the question correctly during the last two chances the loop will break and continue to the next question.
                if user_answer == correct_answer:
                    score +=1
                    break

                # if the answer for each chance is wrong the condition after this else statement will occur. 
                else:
                    print("EEE")
                    continue

            # when the loop ends the question answer's will appear and the next question will appear cause starting new roll. 
            else:

                print(f"{x} + {y} = {correct_answer}")
                continue


    # after ending the 10 question the score will be printed to the user.    
    print(f"Score: {score}")
                     

def get_level():
    while True:

        try:
            level = int(input("Level: ").strip())
            if level not in (1, 2, 3):
                continue

        except ValueError:
            continue

        else:
            return level
        

def generate_integer(level):
    
    if level ==1:
        x = random.randint(0, 9)
    elif level ==2:
        x = random.randint(10, 99)
    elif level ==3:
        x = random.randint(100, 999)

    return x   


if __name__ == "__main__":
    main()
