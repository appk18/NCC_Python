fruit= []
i=0
while i < 3 :
    item = input("Enter 5nos of your favourite : ")
    fruit.append(item)
    i+=1

print("Your favourite  fruit are" , fruit)
yn = input("Do u have any other fruit u like? (Y/N) : ")

if yn == 'Y':
    add_on = input("Enter one more favourite fruit : ")
    fruit.insert(0, add_on)
    print("Total Fav Fruit : ", fruit)
else: 
    print("Total Fav Fruit : ", fruit)

choice = input("Do u want to remove one of ur fav fruit ? (Y/N) : ")
if choice == 'Y':
    remove = input("Enter what u want to remove : ")
    fruit.remove(remove)
    fruit.sort()
    print("Total Fav Fruit after remove : ", fruit)
else:
    fruit.sort()
    print("You did not remove. Total Fav Fruit : ", fruit)





