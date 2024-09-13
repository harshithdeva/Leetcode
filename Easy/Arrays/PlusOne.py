def plusOne(digits):
    l = len(digits)
    s = ""
    for i in range(len(digits)):
       s = s+str(digits[i])
    s = int(s)
    s = s+1
    s = str(s)
    k = []
    for j in s:
        j = int(j)
        k.append(j)
    
    print(k)
        
    ##  Solved on my own

### More Efficient Soltion

#def plusOne(digits):
#    num = 0
#    for i in range(len(digits)):
#    	num += digits[i] * pow(10, (len(digits)-1-i))
#    return [int(i) for i in str(num+1)]

