n=int(input())
inflows=list(map(int,input().split()))

capacity=1000
current=0

for i in range(n):
    current=current+inflows[i]
    if current > capacity:
        print(i+1)
        break
