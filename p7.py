import numpy as np

# lst = np.array(["hello", "Dhaval"])

# print(lst)
# print(type(lst))

# lst = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

# lst = np.arange(1, 10)
# # lst = lst.reshape(3, 3)

# lst.resize(2, 3)

# print(lst)

lst1 = np.arange(1, 13)

lst1 = lst1.reshape(4, 3)

lst2 = np.arange(1, 13)

lst2 = lst2.reshape(3, 4)

lst3 = np.zeros([4, 4], dtype=int)

for i in range(len(lst1)):
    for j in range(len(lst2[0])):
        for k in range(len(lst2)):
            lst3[i][j] += lst1[i][k] * lst2[k][j]

# print(len(lst1))
# print(len(lst2))
# print(len(lst2[0]))
print(lst3)

# data = np.ndarray.tolist(lst3)

# f = open("test.txt", "w")

# for i in data:
#     f.write(str(i))

# f.close()

# f = open("test.txt", "r")
# f.read()
# f.close()

lst3 = np.dot(lst1, lst2)

print(lst3)
