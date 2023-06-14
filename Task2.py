# У вас есть массив чисел, составьте из них максимальное число. Например: [61, 228, 9]

some_list = [61, 228, 9, 8881, 888, 909, 1200, 123, 1, 12, 99]
check_pairs = True
while check_pairs:
    # Run the cycle for comparing elements in pairs
    number_of_shift = 0
    for i in range(0, len(some_list) - 1):
        # comparing nearby elements
        first = str(some_list[i])
        second = str(some_list[i + 1])
        if int(str(first) + str(second)) < int(str(second) + str(first)):
            some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
            number_of_shift += 1
    if number_of_shift == 0:
        check_pairs = False
    print(some_list)
res = ""
for i in some_list:
    res += str(i)
print(res)
