#List Comprehension for string
name_lst = []
i = 0
while i < 5:
    name = input("Enter 8 nos of name : ")
    name_lst.append(name)
    i += 1
print("Your Numbers : " ,name_lst)

e = [e for e in name_lst if e[0]=='p' if e[len(e)-1]=='e']
print(e)


#List Comprehension for int
num_lst = [1,2,3,4,5,6,7,8,9,10]

even = [n for n in num_lst if n%2==0]
print("Even Number : " , even)

odd = [n for n in num_lst if n%2 != 0]
print("Odd Number : ", odd)


#dictinary comprehension
dict = {a: a*2 for a in [1,2,3,4,5]}
print (dict)

key = ['name','age','school']
value = ['Pyae' , 28, 'SIM'] 
my_dict = { k:v for (k,v) in zip(key, value)} 
print (my_dict)


#unpacking
my_list = [2,4,6,8,10]
a, *b = my_list
print(a)
print(b)

*a, b = my_list
print(a)
print(b)
