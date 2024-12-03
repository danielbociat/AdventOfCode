f = open("input3.txt", 'r')
str = f.read()

res = 0
for i in range(len(str)):
    if str[i:i+4] == "mul(":

        j = i+4
        num1 = 0
        num2 = 0
        while j < len(str) and str[j].isdigit():
            num1 = num1*10 + int(str[j])
            j+=1
        
        if num1 > 1000:
            i = i+4
            continue
        
        if j >= len(str) or str[j] != ',':
            continue
        
        j+=1
        while j < len(str) and str[j].isdigit():
            num2 = num2*10 + int(str[j])
            j+=1


        if num2 > 1000:
            i = i+4
            continue
        
        if j >= len(str) or str[j] != ')':
            continue

        res += num1 * num2 

print(res)