import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 77, 8, 9,
                    7, 5, 345, 345, 353, 654, 3415])

for i in range(len(a)):
    print(a[i])
