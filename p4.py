# f = open("test.txt", "w")
# data = "Hello im nick patel"
# f.write(data)
# f.close()

# f = open("test.txt", "r")
# print(f.read())
# f.close()

# hello laxmi screen dikh rahi he type here just two min arjun bhai ate he

f = open("test.txt", "w")


while True:

    data = input("Enter data = ")
    if data == "exit":
        break
    else:
        data = data + " \n "
        f.write(data)

f.close()

f = open("test.txt", "r")
print(f.read())
f.close()
