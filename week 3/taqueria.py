menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0 

while True:
# try to get the input item from the user
    try:
        item = input("Item: ").title()
        total += menu[item]
        print(f"Total: ${total:.2f}")
        
# If user input control-d or control-z like my laptop, catch and finish program
    except EOFError:
        break 
       
# If item not in menu, pass 
    except KeyError:
        pass 
    
