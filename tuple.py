tuple_1 = ('Life', 'is', 'short')
tuple_2 = ('Enjoy', 'it')

tuple = tuple_1 + tuple_2
print(tuple)

print(tuple[:3])
print(tuple[3:])

for t in tuple:
    print(t)

find = input("Enter word that u want to find : ")
no = tuple.count(find)
print("No of",find, "in the list is " , no)
