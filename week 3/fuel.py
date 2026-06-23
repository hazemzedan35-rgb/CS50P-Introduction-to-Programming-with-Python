while True:
    try:
        x, y = input("Fraction: ").split("/")

    except ValueError:
        pass

    else:
        try:
            if int(x) > int(y):
                pass 
            else:
                result = int(x) / int(y) 
                final = result * 100

                if final <= 1:
                    print("E")
                    break

                elif final >= 99:
                    print("F")
                    break

                else:
                    print(f"{round(final)}%")  
                    break

        except (ZeroDivisionError, ValueError):
            pass
