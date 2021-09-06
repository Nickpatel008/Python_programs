f = open("test.txt", "w")

data = input("Enter Data = ")

while True:

    if data == "exit":
        break
    else:
        f.write(data)
        break

f.close()

rf = open("test.txt", "r")
print(rf.read())
rf.close()
