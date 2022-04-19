def maxArea(A, n):
    area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = max(area, min(A[j], A[i]) * (j - i))
    return area

a = [int(n) for n in input("Enter an array: ").split()]

print(maxArea(a, len(a)))