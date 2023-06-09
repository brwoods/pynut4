def updown(N):
    for x in range(1, N):
        yield x
    for x in range(N, 0, -1):
        yield x
for i in updown(3):
    print(i)              # prints: 1 2 3 2 1


def frange(start, stop, stride=1.0):
    start = float(start)
    while start < stop:
        yield start
        start += stride

for f in frange(1, 2, stride=0.125):
    print(f'{f:.3f}')
