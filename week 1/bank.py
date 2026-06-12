user_greating = input("Enter a greeting: ").strip().lower()
if user_greating.startswith("hello"):
    print ("$0")
elif user_greating.startswith("h"):
    print("$20")
else:
    print("$100")