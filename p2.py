print("Primary Number")
num = int(input("Enter Number = "))
if num > 1:
    for i in range(2, num // 2):
        if(num % i) == 0:
            print(num, "Num is not prime numbe.")
            break
        else:
            print(num, "Num is prime numbe.")
    else:
        print(num, "Num is prime numbe.")
