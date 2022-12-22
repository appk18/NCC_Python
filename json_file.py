import json

f = open('data.json',)
data = json.load(f)

input = input("Enter name to see his/her details : ")

data_lst = [] 
for i in data['data']:
    x = i['name']
    if x == input:
        data_lst.append(i)

data_value = [] 
for dic in data_lst:
    value = list(dic.values())
    print(value)

f.close()
