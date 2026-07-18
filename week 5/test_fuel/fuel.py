def main():
    while True:
        user_input = input("Fraction: ").strip()
        try:
            fraction = convert(user_input)
            print(gauge(fraction))
            break
        except (ValueError, ZeroDivisionError):
            continue
        
    
def convert(fraction):
    x, y = fraction.split("/")

    if "/" not in fraction:
        raise ValueError("format the input in a/b form")
    
    if not x.isdigit() or not y.isdigit():
        raise ValueError("enter and integer numbers")
    
    if int(y) ==0:
        raise ZeroDivisionError

    if int(x) > int(y):
            raise ValueError("y should be greater than x")
    
    result = int(x) / int(y) 
    final = result * 100

    return round(final)

    
def gauge(percentage):

    if percentage <= 1:
        return "E"
                    

    elif percentage >= 99:
        return "F"
    
    else:
        return f"{percentage}%"
                    

if __name__ == "__main__":
    main()