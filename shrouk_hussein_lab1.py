# print("Q1")
# while True:
#     string = input("Enter any string to count vowels")
#     counter = 0
#     if string.isspace():
#         print("you must enter string")
#     else:
#         vowels = ["a", "e", "i", "o","u"]
#         for char in vowels:
#             counter += string.lower().count(char)
#         print( "The number of vowels is: ",counter)
#         break
# print("Q2")
# """fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output."""
# array=[]
# for i in range(5):
#     element = input("enter elements of an array")
#     array.append(element)
# print(array)
# array.sort()
# print("ascending: ",array)
# array.sort(reverse=True)
# print("descending: ",array)

# print("Q3")
# while True:
#     string = input("Enter any string")
#     if string.isspace():
#         print("you must enter string")
#     else:
#         counter = string.lower().count("iti")
#         print( "The number of iti occurrence is: ",counter)
#         break

# print("Q4")
# vowels = ["a", "e", "i", "o", "u"]
# while True:
#     string = input("Enter any string")
#     if string.isspace():
#         print("you must enter string")
#     else:
#         updated=""
#         for char in string:
#             if char.lower() not in vowels:
#                 updated += char
#         print(updated)
#         break


# print("Q5")
# while True:
#     string = input("Enter any string")
#     if string.isspace():
#         print("you must enter string")
#     else:
#         for index in range (len(string)):
#             if string[index].lower() == "i":
#                 print(index)
#         break

# print("Q6")
# num = input("enter a number")
# list = []
# if num.isnumeric():
#     for i in range(1,int(num)+1):
#         list2=[]
#         for j in range(1,i+1):
#             list2.append(i * j)
#         list.append(list2)
#     print(list)

# print("Q7")
# num = input("enter a number")
# if num.isnumeric():
#     for i in range(1, int(num) + 1):
#         output = ""
#         for j in range(1,int( num)-i+1):
#             output += " "
#         for j in range(1,i+1):
#             output += "*"
#         print(output)





