# There will be 3 lists output list follows the rule
# if the index is even fill by max no.
# if the index is odd fill by mun no.
# among 3 list

L1 = [10,7,-2,14]
L2 = [-22,11,3,9]
L3 = [1,3,5,4]

O = []

for i in L1,L2,L3:
    if i % 2 == 0:
        O.append(max(L1,L2,L2))
    else:
        O.append(min(L1,L2,L3))
print(O)