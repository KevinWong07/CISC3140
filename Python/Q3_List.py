numList = []
read = True
while read:
    num = float(input("Enter a number or Enter '-1' to quit. "))
    if num == -1:
        read = False
    else:
        numList.append(num)
print("The list is: ")
print(*numList,sep=", ")