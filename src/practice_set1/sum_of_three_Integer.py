def distinct_triplets(arr):
    n=len(arr)
    triplets=set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] +arr[j] + arr[k] == 0 :
                    triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
                    triplets.add(triplet)



    for t in triplets:
        print(t)

if __name__ == "__main__":
    N=int(input("enter the size of array"))
    arr=[]
    print("enter the array elements ")
    for i in range(N):
        arr.append(int(input()))

    distinct_triplets(arr)

