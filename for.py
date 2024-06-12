n = int(input("Enter the number : "))
for i in range(0, n + 1):
    flag = 0
    if i == 0 or i == 1:
        flag = 1
    else:
        for j in range(3, i - 1):
            if (1 % j == 0):
                flag = 1
    if flag == 0:
        print(f'{i}',end='  ' )
        
        
        
        
        
        
        
        
        
        
        
        
        
#  def print_inverse_triangle(size):
# #     for i in range(size, 0, -1):
# #         for j in range(1, i + 1):
# #             print(j, end=' ')
# #         print()
# # print_inverse_triangle(5)
# 
# 
# # def print_inverse_triangle(size):
# #     for i in range(0,5):
# #         for j in range(i):
# #             print('  ', end='')
# #         for j in range(0,5 - i, 0, -1):
# #             print(j, end=' ')
# #         print()
# # print_inverse_triangle(5)











#
#
#
#

#
# a = "Which color is your Bugatti "
# print(a.replace("Bugatti","Bagatata"))
# print(a.split(" "))
#
#
#
#


# for i in a:
#     print(i)
# print()
# print(len(a))


#
#
# txt = "My name is \"Tanu\""
# print(txt)




a = ["Mys", "Man", "Deng"]
a.append("Mang")
print(a)