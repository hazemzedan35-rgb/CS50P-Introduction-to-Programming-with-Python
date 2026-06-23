while True:
    try:
        x, y = input("enter fraction: ").split("/")

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
                elif final >= 99:
                    print("F")
                else:
                    print(f"{final.round()}%")
                break

        except (ZeroDivisionError, ValueError):
            pass
