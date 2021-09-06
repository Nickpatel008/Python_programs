# [] LIST
# () TUPLE
# {} SET
# {:} DICTIONARY

# name = "Dhaval"
# lst = list(name)
# print(type(name))
# print(type(lst))
# print(name)
# print(lst)

# lst = ["abcd", "abcd"]
# for i in lst:
#     print(i)

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [1, 2, 3, 4, 5, 6]

# data = input("data = ")

# lst1.append(data)
# # lst1.remove("a")
# print(lst1)

# lst3 = []

# lst3.append(lst1)
# print(lst3)


# class car:

#     def __init__(self):
#         print("Hello")

#     def sum(self, x=20, y=10):
#         print(x + y)


# class bus(car):
#     def __init__(self):
#         print("Class BUS")

#     def sum(self, a):
#         print(a)


# obj = bus()
# obj.sum(1, 2)


# f = open("test.txt", "w")

# while True:

#     data = input("Enter Data = ")

#     if data == "exit":
#         break
#     else:
#         data = data + "\n"
#         f.write(data)

# f.close()

# while True:
#     ch = int(input("Enter your choice = "))

#     if ch == 0:
#         break
#     elif ch == 1:
#         print("1")
#     elif ch == 2:
#         print("2")
#     elif ch == 3:
#         print("3")
#     else:
#         print("error")
#         break

# class stack:

#     def __init__(self):
#         self.top = -1
#         self.size = 5
#         self.lst = []

#     def push(self, data):
#         if self.top >= self.size - 1:
#             print("Stack overflow...")
#         else:
#             self.lst.append(data)
#             self.top = self.top + 1

#     def pop(self):
#         if self.top < 0:
#             print("Stack is empty")
#         else:
#             re = self.lst[self.top]
#             self.lst.remove(re)
#             self.top = self.top - 1

#     def peep(self):
#         print(self.lst[self.top])

#     def display(self):
#         if self.top >= 0:
#             for i in reversed(self.lst):
#                 print("Data", i)


# s = stack()

# while True:

#     print("1. Push")
#     print("2. Pop")
#     print("3. Peep")
#     print("4. Display")
#     print("5. Exit")

#     inp = int(input("Enter Your Choice = "))

#     if inp == 1:
#         data = int(input("data = "))
#         s.push(data)
#     elif inp == 2:
#         s.pop()
#     elif inp == 3:
#         s.peep()
#     elif inp == 4:
#         s.display()
#     elif inp == 5:
#         exit(0)
#     elif inp >= 6:
#         break

# class demo:

#     def __init__(self, a):
#         self.a = a

#     def __add__(self, o):
#         return self.a + o.a

#     def __sub__(self, o):
#         return self.a - o.a


# d1 = demo(10)
# d2 = demo(5)

# print(d1 + d2)
# print(d1 - d2)
