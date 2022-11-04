def bi_to_deci(binary):
    integer = 0
    i = 0
    while i < len(binary):
        a = int(binary[len(binary) - 1 - i])
        b = a*pow(2,i)
        integer = integer + b
        i+=1
    print(integer)
    
def deci_to_bi(deci):
    binary = 0
    a = 0
    while(deci != 0):
        b= deci%2
        binary = binary + b * (10**a) 
        deci = deci // 2
        a += 1
    print(binary)

choice = int(input("Please choose options\n 1.binary to decimal\n 2.decimal to binary\n Your Choice : "))
if choice == 1:
    binary = input("Please enter binary number : ")
    bi_to_deci(binary)
elif choice == 2:
    deci = int(input("Please enter decimal number : "))
    deci_to_bi(deci)
else:
    print("Wrong input!")

