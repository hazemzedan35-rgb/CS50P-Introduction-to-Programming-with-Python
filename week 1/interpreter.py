x, y, z = input("please input the mathmatical expression with spaces between numbers and signs\n").split()
if y == "+":
    print(f"{float(x) + float(z):.1f}")
elif y == "-":
   print(f"{float(x) - float(z):.1f}")
elif y == "*":
    print(f"{float(x) * float(z):.1f}")
elif y == "/":
    print(f"{float(x) / float(z):.1f}")



