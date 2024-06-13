n = int(input("Enter the value of n : "))
arr = []
print("Enter the value of arr[] :")
for i in range(n):
    arr.append(int(input()))
arr.sort()
i = 0
print("Repeated value:")
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print( arr[i])
