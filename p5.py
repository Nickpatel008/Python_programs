'''

name = "Dhaval"
print(name)

x = list(name)
print(x)

vvl = ["a", "e", "i", "o", "u"]
result = []

while True:
    name = input("Enter your name = ")

    data = list(name)
    print(data)

    for i in data:
        if i in vvl:
            print(i)
            result.append(i)
        else:
            pass

    print(result)
'''

lst1 = ["Dhaval", "muskan", "rohit"]
lst2 = ["Dhaval", "rohit"]
lst3 = []
# for i in lst1:
#     # print(i)
#     for j in lst2:
#         if i == j:
#             lst3.append(j)
#             print("match", lst3)
#         else:
#             pass


# set1 = set(lst1)
# set2 = set(lst2)

# data = list(set1 & set2)

# print(data)

# f = open("test.txt", "w")
# for i in data:
#     f.write(i + " ")

# f.close()

# rf = open("test.txt", "r")
# print(rf.read())
# rf.close()

# set1 = set(lst1)
# set2 = set(lst2)
# data1 = set1 - set2
# data2 = set1 ^ set2
# data3 = set1 & set2
# data4 = set1 | set2

# print(data1)
# print(data2)
# print(data3)
# print(data4)

# f = open("test.txt", "w")

# while True:
#     data = input("Write data [ 'exit' for Exit ] = ")

#     if data == "exit":
#         break
#     else:
#         data = data + "\n"
#         f.write(data)

# f.close()

# f = open("test.txt", "r")

# for i in range(5):
#     print(f.readline().rstrip())

# f.close()

# f = open("test.txt", "r")

# s = int(input("Start line number = "))
# e = int(input("end line number = "))

# for i in range(s, e):
#     print(f.readline().rstrip())

# f.close()

# f = open("test.txt", "r")
# n = 1
# for i in f:
#     print(n, len(list(i.rstrip().split())))
#     n += 1

# f.close()


# f = open("test.txt", "r")

# for i in f:
#     t = list(i.rstrip().split())
#     t.reverse()

#     for j in t:
#         print(j, end=" ")
#     print("")

# f.close()


# f = open("test.txt", "r")
# data = []

# for i in f:
#     t = list(i.rstrip().split())
#     char = 0
#     digits = 0
#     for j in t:
#         if j.isalpha():
#             char = 1
#         else:
#             digits = 1
#     if char == 1 and digits == 1:
#         data = i.rstrip()
#         print(i.rstrip())


# f.close()

# print("*"*10)
# f = open("test1.txt", "r")
# f.read()
# f.close()
