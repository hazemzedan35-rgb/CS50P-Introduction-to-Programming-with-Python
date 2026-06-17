amount_due = 50 

while  True:
    insert_coin = int(input("insert coin: "))
    if insert_coin in [5, 10, 25]:
        amount_due -= insert_coin

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
          
        elif amount_due == 0:
            print(f"Change Owed: {amount_due}")
            break

        elif amount_due < 0:
            amount_due = amount_due - 2*amount_due
            print(f"Change Owed: {amount_due}")
            break
        
    else:
        print(f"Amount Due: {amount_due}")
        
    

       
        