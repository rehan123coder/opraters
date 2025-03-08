row=int(input("please enter the total number of rows"))
print("floyed triangle")
no=1
for i in range(1, row + 1):
    for j in range(1,i+1):
        print(no,end=" ")
        no=no+1
    print()