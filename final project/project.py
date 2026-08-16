import sys

def main():
    temprature = get_temprature()
    humidity = get_humidity()

    checked_temprature = check_temprature(temprature)
    checked_humidity = check_humidity(humidity)

    hive_status = check_hive_status(checked_temprature, checked_humidity)

    print(hive_status)

def get_temprature():
    try:
        temp = float(input("Enter the hive temprature (without '^C' sign): "))
    except ValueError:
        sys.exit("Temprature must be in numbers!!")
    else:
        return temp


def get_humidity():
    try:
        humi = float(input("Enter the hive humidity(without '%' sign): "))
    except ValueError:
        sys.exit("Humidity must be in numbers!!")
    else:
        return humi


def check_temprature(temprature):
    if 33.0 <= temprature <= 36.0:
        return True
    else:
        return False


def check_humidity(humidity):
    if 50.0 <= humidity <= 70.0:
        return True
    else:
        return False
    

def check_hive_status(temprature, humidity):
    if temprature and humidity:
        return "Status: Optimal (Hive is healthy)."
    
    elif temprature and not humidity:
        return "Status: warning humidity in hive isn't in the normal state."
    
    elif not  temprature and humidity:
        return "Status: warning temprature in hive isn't in the normal state."

    else:
        return "Status: Both temprature and humidity aren't in normal state "



if __name__=="__main__":
    main()