#Binary Search with iterative method 
num_lst = []
i = 0
while i < 5:
    num = int(input("Enter 8 nos of number : "))
    num_lst.append(num)
    i += 1
print("Your Numbers : " ,num_lst)

n = int(input("Choose one number : "))
print("You choose : ", n)

def cal(arr,a):
    low = 0 
    mid = 0
    high = len(arr)-1
    
    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] < a:
            low = mid + 1

        elif arr[mid] > a:
            high = mid - 1
 
        else:
            return mid
    return -1

result = cal(num_lst, n)
 
if result != -1:
    print("Element is at index", result)
else:
    print("Element is not in the array")