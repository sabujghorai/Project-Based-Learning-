# Write a python program to count frequency of each character
# PROGRAMMING.   P-1, R-2, 0-1, G-2, A-1, M-2, I-1, N-1

L = input("Enter string :")
s = {}
for ch in L:
    if ch in s:
        s[ch] = s[ch] + 1
    else:
        s[ch] = 1

for ch in s:
    print(ch,":", s[ch])