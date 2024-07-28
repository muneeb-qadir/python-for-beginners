def sum_all(*args):
  print(args) #Tupple
  for i in args:
    print(i*3)
  return  sum(args)

print(sum_all(1,2,3,4))
# print(sum_all(1,2,5,6))
# print(sum_all(1,2,3,4,5,6,7))