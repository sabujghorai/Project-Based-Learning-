import math
# Write a python program to display the elements of a given list in the 
# following meanner
# [-ve, all zeros, +ve]
# L = [4,-7,0,0,3,-2,5,0,1]
# Output --- [-7, -2, 0, 0, 0, 4, 3, 5, 1]

L = [4,-7,0,0,3,-2,5,0,1]
A = []
p =[]
q = []
for i in range(len(L)):
    if L[i] < 0:
        A.append(L[i])
    elif L[i] == 0:
        p.append(L[i])
    else:
        q.append(L[i])
print(A+p+q)




# There will be 3 lists output list follows the rule
# if the index is even fill by max no.
# if the index is odd fill by mun no.
# among 3 list

L1 = [10,7,-2,14]
L2 = [-22,11,3,9]
L3 = [1,3,5,4]

O = []

for i in range(len(L1)):
    if i % 2 == 0:
        O.append(max(L1[i],L2[i],L3[i]))
    else:
        O.append(min(L1[i],L2[i],L3[i]))
print(O)




# no of possible permutaion of elements A = [1,2,3] of these elements 
# Output = [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
A = [1, 2, 3]
B = []


for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if i != j and j != k and i != k:
                permutation = [A[i], A[j], A[k]]
                B.append(permutation)

print(B)
