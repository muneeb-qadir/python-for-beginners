numbers, range_list = [int(x) for x in input("Enter a list of integers separated by commas: ").split(',')], list(range(0, 11))
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Final Count of Positive Number is: ", positive_number_count)
