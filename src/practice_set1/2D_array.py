def read_2d_array():

    rows=int(input("Enter rows: "))
    cols=int(input("Enter columns:"))

    arr_2d=[]

    print("Enter the elements of the array")
    for i in range(rows):
        row=[]
        for j in range(cols):
            ele=float(input(f"Enter the element [{i}][{j}]:"))
            row.append(ele)
        arr_2d.append(row)
    return arr_2d

def main(arr_2d):
    for row in arr_2d:
        for item in row:
            print(item, end=" ")
        print()

if __name__ == "__main__":
    main(read_2d_array())
