#  simple password validator
#  RULES
#  should be more than 8 letters 
#  must contain 2 of smth thats not a alphabet i.e num or character 
#  atleast one uppercase

def leng(pwrd):
    if len(pwrd) >= 8:
        return True
    else:
        return False
    
def non_alpha(pwrd):
    a=0
    for i in list(pwrd):
        if i.isalpha() == False:
            a+=1
    if a > 0:
        return True
    else:
        return False

def upppercase(pwrd):
    a = 0
    for i in list(pwrd):
        if i.isalpha() == True and i.isupper() == True:
            a+=1
    if a > 0:
        return True
    else:
        return False

b = 0
while b >= 0:
    if b ==0:
        print("Provide a password and We will do some checks for it \n1. It should be more than 8 letters \n2. Atleast one non alphabet \n3. atleast one uppercase")
        pwrd = input("Please Enter your password : ")
    else:
        pwrd = input("Please Re-Enter your password : ")
        print("lets Re-evaluate if the New Password is good enough or not.")

    if leng(pwrd) ==True:
        print("Alright it passes first check it has", len(pwrd),"words")
    else:
        print("Bruh make it atleast 8 letter")
        b+=1
        continue

    if non_alpha(pwrd) ==True:
        print("Oho alright it passes out the second Check Tooo")
    else:
        print("brother just add a non alphabet")        
        b+=1
        continue    
    
    if upppercase(pwrd) ==True:
        print("Oho alright it passes out the Third Check YESSS ")
    else:
        print("brother just add a Capital word")
        b+=1
        continue
    
    print("Yes now your password fits our category :D")
    b = -1
    break
