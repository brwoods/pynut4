x = [1, 2, 3, 4]
x[1] = 42                # x is now [1, 42, 3, 4]

x = [1, 2, 3, 4]
x[1:3] = [22, 33, 44]     # x is now [1, 22, 33, 44, 4]
x[1:4] = [8, 9]           # x is now [1, 8, 9, 4]

x = [1, 2, 3, 4, 5]
del x[1]                 # x is now [1, 3, 4, 5]
del x[::2]               # x is now [3, 5]
