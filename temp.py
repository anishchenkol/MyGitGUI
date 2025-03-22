# объявление функции
#def is_primitive(num):
    
# объявление функции
def is_prime(num):
    f = True
    if num == 1:
       return False
    for i in range(2,num//2+1):
        if num%i == 0:
            f = False
            break
    return f    

def is_palindrome(num):
    temp = str(num)
    for i in range(len(temp)//2):
        
        if temp[i] != temp[-1 - i]:
            return False
            break
    return True 
    
def is_valid_password(password):
    f = True
    s =[]
    for c in password.split(':'):
        s.append(int(c)) 
    #print(s)
    if len(s )!=3:
        return False
    elif not is_prime(s[1]):
        return False
    elif s[2]%2==1:
        return False
    elif not is_palindrome(s[0]):
        return False
    # s.append(int(c) )
    return f    
# считываем данные
psw = '15551:7:290'
psw = '155561:7:290'



# вызываем функцию
print(is_valid_password(psw))