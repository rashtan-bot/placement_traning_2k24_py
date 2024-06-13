a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
ad = a - (- b)
print("The sum of a and b is", ad)

x = int(input("Enter the value of first number "))
y = int(input("Enter the value of second number "))
q = x // y
if q < 0:
    q += 1

mod = x - (q * y)
print("The mod of ", x, "and", y, "is", mod)

# find division of two numbers without using mod or devison symbol
# 13 2 6
# 14 -2 -7
# -11 2 -5
# ?hint multiple if and while
