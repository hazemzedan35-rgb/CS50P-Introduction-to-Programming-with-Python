import inflect

plural = inflect.engine()
final_list = []

while True:
    try:
        name_list = input("Name: ")
        final_list.append(name_list)
    except EOFError:
        print()
        break
output = plural.join(final_list)

print(f"Adieu, adieu, to {output}")

