import random

#for user input 
user_num=[]
for i in range(0,5):
        user_input = int(input("Please enter 5 numbers : "))
        user_num.append(user_input)

# #for lot number
lot_num = []
for i in range(0,5):
    ran_num = random.randint(0,99)
    lot_num.append(ran_num)

#check no of correct numbers
correct_num = 0
for res in lot_num:
    for inp in user_num:
        if res == inp:
            correct_num = correct_num + 1

if (correct_num == 1):
    win_amount = (10000 * 0.02)
elif(correct_num == 2):
    win_amount = (10000 * 0.05)
elif(correct_num == 3):
    win_amount = (10000 * 0.1)
elif(correct_num == 4):
    win_amount = (10000 * 0.2)
elif(correct_num == 5):
    win_amount = (10000 * 0.5)
elif(correct_num == 6):
    win_amount = 10000
else:
    win_amount = 0

if __name__ == "__main__":
    print("User betting number is ", user_num)
    print("Winning Number is ", lot_num)
    print("No of correct number : ", correct_num )
    print("The price is $10000 and You win $", win_amount)
    

