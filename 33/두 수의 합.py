import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())

arr.sort()

i = 0
j = 0

count = 0

while i != n - 1 or j != n - 1:
    if i == j:
        j += 1
    if arr[i] + arr[j] == x:
        count += 1
    else:
        if j == n - 1:
            j = 0
            i += 1
        else:
            j += 1
    print(count)

print(count)
