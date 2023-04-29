stroka = ""

for i in range(26):
    for j in range(26):
        stroka = stroka + (chr(ord('a') + i)) + (chr(ord('a') + j)) + " "

print(stroka)
