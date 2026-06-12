def main():
    time = convert(input("what time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
def convert(time):
    Hours, Minutes = time.split(":")
    if "pm" in Minutes:
        system_12_minutes, pm = Minutes.split()
        if int(Hours) != 12:
            system_12 = int(Hours) + 12
        else:
            system_12 = int(Hours)
    elif "am" in Minutes:
        system_12_minutes, am = Minutes.split()
        if int(Hours) != 12:
            system_12 = Hours
        else:
            system_12 = 0
    else:
        system_12 = Hours
        system_12_minutes = Minutes
    time_table = float(system_12) + float(system_12_minutes) / 60
    return time_table
if __name__ == "__main__":
    main()
