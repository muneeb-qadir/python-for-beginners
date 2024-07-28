items, range_list = [(x) for x in input("Enter a list separated by commas: ").split(',')], list(range(0, 11))

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
     
