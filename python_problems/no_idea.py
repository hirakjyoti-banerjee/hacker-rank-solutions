n,m = input().split()

array = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))

count=0

for i in array:
    if i in a:
        count = count + 1
    if i in b:
        count = count - 1

print(count)
