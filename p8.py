# with open("test.txt", "w") as f:

#     while True:
#         data = input("Enter Data = ")

#         if data == "exit":
#             break
#         else:
#             data = data + "\n"
#             f.write(data)


from typing import Counter


with open("test.txt", "r") as f:

    def get_line():

        count = 0
        d = f.read()
        data = d.split("\n")

        for i in data:
            count += 1

        # print(d.rstrip())
        print("Number of total lines = ", count)

    def get_empty_lines():
        count = 0
        data = f.readlines()

        for i in data:
            if i == "\n":
                print("Empty Line Here")
                count += 1
        print(count)

    def char_digit_lines():
        # count = 0
        # data = f.readline()

        for i in f:
            lines = list(i.rstrip().split())
            a = 0
            d = 0

            for j in lines:
                if j.isalpha():
                    a = 1
                else:
                    d = 1
            if a == 1 and d == 1:
                print(i.rstrip())

    def reversed_llines():

        # lines = f.read()
        lines2 = f.readlines()

        # data = lines[::-1]
        data2 = lines2[::-1]

        # print(data)
        print(data2)

    while True:

        inp = int(input("Enter Choice = "))

        if inp == 0:
            print("Exit")
        elif inp == 1:
            get_line()
        elif inp == 2:
            get_empty_lines()
        elif inp == 3:
            char_digit_lines()
        elif inp == 4:
            reversed_llines()
