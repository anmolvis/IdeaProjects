day = {"mon": 1, "tues": 2, "wed": 3, "thurs": 4, "fri": 5, "sat": 6, "sun": 7}
num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
T = int(input())
for i in range(T):
    q = input()
    W, s = int(q[0:2]), q[3:q.__len__()]
    x = day.get(s)
    for j in range(1, W+1):
        if x == 8:
            x = 1
        num[x] = num[x] + 1
        x = x + 1
    print(num[1], num[2], num[3], num[4], num[5], num[6], num[7])
    for j in range(1, 8):
        num[j] = 0
