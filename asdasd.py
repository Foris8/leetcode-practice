X = [0] * 256
count = 0


def mia(a, b, c):
    global count  # Declare 'count' as global
    if c > b:
        count += 1
        
    else:
        for i in range(X[c - 1] + 1, a + 1):
            X[c] = i
            mia(a, b, c + 1)


mia(321, 21, 1)
print("Count:", count)
