
def bubble_sort(arr):  
    for i in range(0,len(arr)-1):  
        for j in range(len(arr)-1):  
            if(arr[j]>arr[j+1]):  
                temp = arr[j]  
                arr[j] = arr[j+1]  
                arr[j+1] = temp  
    return arr   

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
 
no = int(input("No of elements : "))
i = 0
list = []
while i < no:
    num = int(input("Please enter digit : "))
    list.append(num)
    i+=1
print("The sorted list is: ", bubble_sort(list))  

find_no = int(input("Please enter an element u want to serach : "))

res = binary_search(list, find_no)
if res != -1:
    print("Element is at index", res)
else:
    print("Element is not in the array!")