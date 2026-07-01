month_in_letters = {
"January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June":6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12

}
    

while True:

    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            if int(month) <= 12 and int(day) <= 31:
                print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
                break

        elif "," in date:
            month, day, year = date.split(" ")
            day = day.strip(",")
            if month in month_in_letters and int(day) <= 31:
                print(f"{int(year):04d}-{month_in_letters[month]:02d}-{int(day):02d}")
                break

    except ValueError:
        continue
    
