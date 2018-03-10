# This is the optimize code as the commented code exceeded the time limit
# which is given in code chef\
# By Anmol Agarwal

import math
T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    str3 = input()
    N, Q = str1.split()
    D = str2.split()
    X = str3.split()
    # for j in range(int(Q)):
    #     for k in range(int(N)):
    #         X[j] = math.floor(int(X[j]) / int(D[k]))
    #     print(X[j], " ", end="")
    # print()
    m = 1
    for j in range(int(N)):
        m = m * int(D[j])
    for j in range(int(Q)):
        print(math.floor(int(X[j]) / m), " ", end="")
    print()
