# n = int(input("Enter the value of n : "))
# arr = []
# print("Enter the value of arr[] :")
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# # for i in range(n):
# #     for j in range(i + 1, n):
# #         if arr[i] == arr[j]:
# #             print( arr[i])
# print("Result")
# # for i in range(n):
# #     if(arr[i]==arr[i-1]):
# #         if(arr[i-1]>arr[i]):
#
#
# print(arr[n-2])















n = int(input("Enter the value of n: "))
arr = []
print("Enter the values of arr:")
for i in range(n):
    arr.append(int(input()))
unique_elements = list(set(arr))
unique_elements.sort()
if len(unique_elements) >= 2:
    print("Result:", unique_elements[-2])
else:
    print("Result: -1")
