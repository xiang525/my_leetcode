"""
snapchat interview question
input a,b are strings
数太大， 一位一位的来加
"""
def add(a,b):
    res = ''
    carry = 0
    n = min(len(a),len(b))
    a = a[::-1]
    b = b[::-1]
    
    for i in range(n):      
        
        res += str((int(a[i])+int(b[i])+carry)%10)
        carry = (int(a[i])+int(b[i])+carry)/10
    if a:
        for k in a[n:]:
            
            res+=str((carry+int(k))%10)
            carry = (carry+int(k))/10
    if b:
        for k in b[n:]:
            
            
            res += str((carry+int(k))%10)
            carry = (carry+int(k))/10
    if carry == 1:        
        res += '1'   
    
    return ''.join(res[::-1])


if __name__ == "__main__":
    a = '82'
    b = '18'
    print add(a,b)
    
    












