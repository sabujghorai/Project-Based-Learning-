# Write a python program to display the elements of a given list in the following meanner
# [-ve, all zeros, +ve] 
# L = [4,-7,0,0,3,-2,5,0,1]
# Output --- [-7, -2, 0, 0, 0, 4, 3, 5, 1]

L = [4,-7,0,0,3,-2,5,0,1]
L1 = []
p =[]
q = []
for i in range(len(L)):
    if L[i] < 0:
        L1.append(L[i])
    elif L[i] == 0:
        p.append(L[i])
    else:
        q.append(L[i])
print(L1+p+q)