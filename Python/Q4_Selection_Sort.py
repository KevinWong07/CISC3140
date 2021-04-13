A = [5, 6,1, 2, 8, 9, 12, 18, 7, 10]
print("Original Unsorted Array:")
print(A)
for i in range(len(A)):
    min_ele = i
    for j in range(i + 1, len(A)):
        if A[min_ele] > A[j]:
            min_ele = j

    A[i], A[min_ele] = A[min_ele], A[i]
print("Sorted Array:")
print(A)