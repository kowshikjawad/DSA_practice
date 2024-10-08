s = "axc"
t = "ahxgdc"



j =  0

for i in t:
    if i == s[j]:
        j += 1
    if j == len(s):
        return True


