import re


def main():
    hours = input("Hours: ")
    print(convert(hours))


def check_input(time):
    if matches := re.search(r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(PM|AM)$", time):
        if  int(matches.group(1)) == 0:
            raise ValueError
        if int(matches.group(4)) == 0:
            raise ValueError

        if matches.group(2) == None:
            h2 = "00"
        elif int(matches.group(2)) > 59:
            raise ValueError
        else:
            h2 = matches.group(2)

        if matches.group(5) == None:
            h5 = "00"
        elif int(matches.group(5)) > 59:
            raise ValueError
        else:
            h5 = matches.group(5)

        if int(matches.group(1)) > 12:
            raise ValueError
        if int(matches.group(4)) > 12:
            raise ValueError
        h1 = matches.group(1)
        h3 = matches.group(3)
        h4 = matches.group(4)
        h6 = matches.group(6)
        return h1, h2, h3, h4, h5, h6 
    else:
            raise ValueError
        


def convert(s):
    h1, h2, h3, h4, h5, h6 = check_input(s)
    if  h3 == "AM" and int(h1) == 12:
        h1 =  "00"
    elif h3 == "PM":
        if int(h1) == 12:
            h1 = h1
        else:
            h1 = str(int(h1) + 12)

    if h6 == "AM" and int(h4) == 12:
        h4 = "00"
    elif h6 == "PM":
        if int(h4) == 12:
            h4 = h4
        else:
            h4 = str(int(h4) + 12)

    if len(h1) == 1:
        h1 = "0" + h1

    if len(h4) == 1:
        h4 = "0" + h4
    
    return f"{h1}:{h2} to {h4}:{h5}"
    
         

if __name__ == "__main__":
    main()
