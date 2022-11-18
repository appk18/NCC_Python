from datetime import date
import random

#User's name
fname = input("Please enter first name : ")
lname = input("Please enter last name : ")
full_name = lambda first, last: first + last

#User DOB
dob = int(input("Enter your date of birth (year) : "))
current_year = date.today().year
checkage = lambda a: current_year - a
age = checkage(dob)

#Calculate Ticket Price
def calprice(type):
    ticket_num = int(input("How many Ticket you want? : "))
    if type == 1 or type == 2:   
        total_amount = lambda t : t * 15
    elif type == 3 or type == 5:
        total_amount = lambda t : t * 20
    else:
        total_amount = lambda t : t * 12
    print(f'Total amount will be ${total_amount(ticket_num)}')

    i = 0
    ticket = []
    while i < ticket_num:
        t = random.randint(1,99)
        ticket.append(t)
        i+=1

    j = 0
    while j < len(ticket):
        print(f'Tikcet No {j+1} : {ticket[j]}')
        j+=1

#Main 
print(f"\t\t Hello, {full_name(fname,lname)}! Welcome to HaveFun Cinema")
print("", "-" *65, "")

if age > 16:
    print(f'You are {age} years old. You can proceed to buy ticket!')
    print("Movie Types\n1. Action\n2. Drama\n3. Horror\n4. Anemie\n5. Supernatural")
    choice = int(input("Please choose movie type : "))
    calprice(choice)
    print("Have Fun!!!")
else:
    print("You are too young to watch movies!")













