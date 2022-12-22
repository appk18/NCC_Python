with open ("data.txt", "r") as myfile:
    lines = myfile.readlines() 

all_name = []
for name in lines:
        if 'Name' in name:
            all_name.append(name)

n = [nm[7:-1] for nm in all_name]

print(n)

