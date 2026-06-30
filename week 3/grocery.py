list_of_items = {}
while True:
    try:
        item = input().upper().strip()
        list_of_items[item] = list_of_items.get(item, 0) + 1
    except EOFError:
        break
for item in sorted(list_of_items):
    print(list_of_items[item], item)
