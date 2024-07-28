numbers, range_list = [int(x) for x in input("Enter a list of integers separated by commas: ").split(',')], list(range(0, 11))
sum_even = 0

for i in numbers:
     if i % 2 == 0:
          sum_even = sum_even+1

print("Sum of Even Numbers is: ",sum_even)