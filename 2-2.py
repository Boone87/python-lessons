my_list = [10,12,55,33,11,6]
list
a = 0
for i in range(int(len(my_list)/2)):
        my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
        a += 2
print(my_list)
