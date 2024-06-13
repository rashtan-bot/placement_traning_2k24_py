N = int(input("Enter the value of N "))

large = 0
for i in range(2, N+1):
    if N % i == 0:
        flag = prime(i)
        if flag==1:
            large=i
print(large)
