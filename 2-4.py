text = input("Введите предложение ")
my_word = []
num = 1
for i in range(text.count(' ') + 1):
    my_word = text.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [i]}")
        num += 1
    else:
        print(f" {num} {my_word [i] [0:10]}")
        num += 1