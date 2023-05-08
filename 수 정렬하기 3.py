import sys
N = int(input())

nlist = list()
for x in range(N):
    nlist.append(int(sys.stdin.readline()))

nlist.sort()
for x in nlist:
    print(x)

