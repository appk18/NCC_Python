import json

input_name = input("Enter new name : ")
input_job = input("Enter new job : ")
input_age = input("Enter new age : ")

new_data = {"name": input_name,
            "job": input_job,
            "age": input_age
    }

with open('data.json','r+') as file:
    fdata = json.load(file)
    fdata["data"].append(new_data)
    file.seek(0)
    json.dump(fdata, file, indent = 4)
