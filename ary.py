n = int(input("Enter the value of n : "))
arr = []
print("Enter the value of arr[] :")
for i in range(n - 1):
    arr.append(int(input()))
arr.sort()
pre = 0
for x in arr:
    if pre + 1 == x:
        pre = x
    else:
        break
print("Missing value is :", pre + 1)
