# weight_lower_limit = 75.5
# weight_higer_limit = 100.0

# weight = float(input("enter your weight: "))

# if weight > weight_higer_limit:
#     if weight > 125.5:
#         print("what the f..k")
#     print("mindaugas is kebab")
# elif weight < weight_lower_limit:
#     print("mindaugas is hungry")
# else:
#     print("mindaugas is cool")




# if weight > weight_higer_limit:
#     print("mindaugas is kebab")
# elif weight < weight_lower_limit:
#     print("mindaugas is hungry")
# else:
#     print("mindaugas is cool")
# print("test is succesfull")



# # 1. Create a program, which takes 10 random numbers. The program should produce
# a list of non primary and tuple of primary numbers. After input is done, program should return the the mathematical
# differnce between the highest and lowest number from non primary numbers, and sum of primary numbers from tuple.


# first_number = int(input("enter your first number: "))
# second_number = int(input("enter your second number: "))
# third_number = int(input("enter your third number: "))


# my_list = []
# my_tuple = (first_number, second_number, third_number)
# my_list.append(first_number)
# my_list.append(second_number)
# my_list.append(third_number)

# print(my_list)
# print(my_tuple)




nr_1 = int(input("Enter 1 no: "))
nr_2 = int(input("Enter 2 no: "))
nr_3 = int(input("Enter 3 no: "))
nr_4 = int(input("Enter 4 no: "))
nr_5 = int(input("Enter 5 no: "))
nr_6 = int(input("Enter 6 no: "))
nr_7 = int(input("Enter 7 no: "))
nr_8 = int(input("Enter 8 no: "))
nr_9 = int(input("Enter 9 no: "))
nr_10 = int(input("Enter 10 no: "))

my_list = []
my_tuple_list = []

if nr_1 < 50:
    my_list.append(nr_1)
else:
    my_tuple_list.append(nr_1)
if nr_2 < 50:
    my_list.append(nr_2)
else:
    my_tuple_list.append(nr_2)
if nr_3 < 50:
    my_list.append(nr_3)
else:
    my_tuple_list.append(nr_3)
if nr_4 < 50:
    my_list.append(nr_4)
else:
    my_tuple_list.append(nr_4)
if nr_5 < 50:
    my_list.append(nr_5)
else:
    my_tuple_list.append(nr_5)
if nr_6 < 50:
    my_list.append(nr_6)
else:
    my_tuple_list.append(nr_6)
if nr_7 < 50:
    my_list.append(nr_7)
else:
    my_tuple_list.append(nr_7)
if nr_8 < 50:
    my_list.append(nr_8)
else:
    my_tuple_list.append(nr_8)
if nr_9 < 50:
    my_list.append(nr_9)
else:
    my_tuple_list.append(nr_9)
if nr_10 < 50:
    my_list.append(nr_10)
else:
    my_tuple_list.append(nr_10)

print(my_list)
print(tuple(my_tuple_list))

print(max(my_list) - min(my_list))
print(sum(my_tuple_list))















 
