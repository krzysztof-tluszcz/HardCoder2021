
#VARIABLES
a=[]
line=""
var = 0

#INPUT
print("Insert a text:")
txt_temp = input()
txt = txt_temp.lower()
t = list(txt)

#TEXT FORMATTING AND PRINTING
for i in range(len(txt)):
    flag = t[i].isalpha()
    if(str(flag) == "False"):
        a.append(i)

for i in range(len(a)):
    t.pop(a[i]-i)

for i in range(len(t)):
    line += t[len(t)-i-1]
print(line)

#PALINDROME CHECK

    #EVEN
if(len(t) % 2 == 0):
    for i in range(int(len(t)/2)):
        if(t[i]==t[len(t)-i-1]):
            var += 1
    if(var == len(t)/2):
        print("It's a palindrome!")
    else:
        print("It's N O T a palindrome!")

    #ODD
else:
    for i in range(int((len(t)+1)/2 - 1)):
        if(t[i]==t[len(t)-i-1]):
            var += 1
    if(var == (len(t)+1)/2 - 1):
        print("It's a palindrome!")
    else:
        print("It's N O T a palindrome!")