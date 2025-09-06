############################################
# Space of 6 means totally new code 
# space of 1 means same code
############################################






#grade calculator
# #??
# Sub1 = ['Physics','Chemistry','Maths','Computer Science', 'English']
# Sub2 = ['Physics','Chemistry','Maths','Biology', 'English']
# Sub3 = ['Physics','Chemistry','Hindi','Biology', 'English']

# print( "What subject do you study? Select from below \nPCM" , Sub1 , "\nPCMB" ,Sub2 , "\nPCB" , Sub3 ,"\nEnter 1 2 3 respectively to select your subect")
# Class = int(input())
# print()
# dict = {}

# def total(sub):
#     totally = 0
#     for i in range(len(sub)):
#         print("Please enter your marks in",sub[i],end = " : ")
#         a = float(input())
#         if a <= 33:
#             dict[sub[i]] = "FAILED"
#         else:
#             dict[sub[i]] = "PASSED!!!!"
#         totally = totally + a
#     return (totally/5)

# def ask_sub(Class):
#     if Class == 1:
#         a = total(Sub1)
#     elif Class == 2:
#         a = total(Sub2)
#     else:
#         a = total(Sub3)
#     return a

# marks = ask_sub(Class)
# print("\nYour final average marks are : ", marks, "\n")

# if marks >= 90:
#     print("Your final grade is A\n")
# elif marks >= 80:
#     print("Your final grade is B\n")
# elif marks >= 70:
#     print("Your final grade is C\n")
# elif marks >= 60:
#     print("Your final grade is D\n")
# else:
#     print("I would quit studying atp\n")

# print("About your subjects : \n")
# for i in dict:
#     print(i + " : " + dict[i])

# #if subject not present
# # ask the people their subjects






# #simple alarm checker
# a = input("What day do you wanna check? ")
# if a.lower() == 'sunday':
#     print("Sleep in!")
# elif a != "Sunday" :
#     Vac = input("Are you on vacation? Y/N ")
#     if Vac in ['Y','y']:
#         print("Its not Sunday But Vacation is on so wake up at 10AM")
#     else:
#         print("Its not Sunday Wake up at 7AM")







# #simple simple calculator?
# Num1 = int(input("enter first number : "))
# Num2= int(input("enter second number : "))
# a = input("what operation do you wanna do ? ")
# if a == '*':
#     print("here is the Multiplication of two numbers : " ,Num1 * Num2)
# elif a == '+':
#     print("here is the Addition of two  : " ,Num1 + Num2)
# elif a == '-':
#     print("here is the Subtraction of two  : " ,Num1 - Num2)
# elif a == '/' and Num2 != 0:
#    print("Result:", Num1 / Num2)
# elif a == '/' and Num2 == 0:
#    print("Can't divide by zero!")






# #Even odd detector easy
# a = int(input("whats the number you wanna check? "))
# if a % 2 == 0:
#     print(a ,"is even")
# else:
#     print(a ,"is odd")






# #Random number guesser
# import random
# while True:
#     num = int(input("""Whats your random guess of a number from 1 - 100?
# (In order to win your guess must be in 20numbers of the number)
# : """))
#     a = random.randint(1,100)
#     if num == a:
#         print("Hey You WON!! , And naah man you must be cheating how you got that right")
#         break
#     elif a in range(num-10,num+10):
#         print("Hey You WON!! , And Damm Thats pretty fucking close to" , a)
#         break
#     elif a in range(num-20,num+20):
#         print("Hey You WON!! , And Damm Not that close but nice try man" , a)
#         break
#     else:
#         print("i mean sure its not even close to like 20 digits so lets just say you lose and start over") 






# #simple password validator
# #should be more than 8 letters , must contain 2 of smth thats not a alphabet i.e num or character, atleast one uppercase
# def leng(pwrd):
#     if len(pwrd) >= 8:
#         return True
#     else:
#         return False
    
# def non_alpha(pwrd):
#     a=0
#     for i in list(pwrd):
#         if i.isalpha() == False:
#             a+=1
#     if a > 0:
#         return True
#     else:
#         return False

# def upppercase(pwrd):
#     a = 0
#     for i in list(pwrd):
#         if i.isalpha() == True and i.isupper() == True:
#             a+=1
#     if a > 0:
#         return True
#     else:
#         return False

# b = 0
# while b >= 0:
#     if b ==0:
#         print("Provide a password and We will do some checks for it \n1. It should be more than 8 letters \n2. Atleast one non alphabet \n3. atleast one uppercase")
#         pwrd = input("Please Enter your password : ")
#     else:
#         pwrd = input("Please Re-Enter your password : ")
#         print("lets Re-evaluate if the New Password is good enough or not.")

#     if leng(pwrd) ==True:
#         print("Alright it passes first check it has", len(pwrd),"words")
#     else:
#         print("Bruh make it atleast 8 letter")
#         b+=1
#         continue

#     if non_alpha(pwrd) ==True:
#         print("Oho alright it passes out the second Check Tooo")
#     else:
#         print("brother just add a non alphabet")        
#         b+=1
#         continue    
    
#     if upppercase(pwrd) ==True:
#         print("Oho alright it passes out the Third Check YESSS ")
#     else:
#         print("brother just add a Capital word")
#         b+=1
#         continue
    
#     print("Yes now your password fits our category :D")
#     b = -1
#     break






# #leap year checker but not a century leap year
# a = int(input("what year do you wanna check for? "))
# if a % 4 == 0:
#     if a % 100 == 0:
#         if a % 400 == 0:
#             print("its a leap year!")
#         else:
#             print("its not a leap year acc to official rules dont kill me man")
#     else:
#         print("its a leap year!")
# else:
#     print("its not a leap year ;/")






# #prime number checker
# a = int(input("what number do you wanna check for? "))
# b=0
# for i in range(3,a):
#     if a % i == 0:
#         b+=1
# if b == 0:
#     print("yess its a prime")
# else:
#     print("its not a prime")






# #lucky whatever
# num = input("enter the numbers you wanna enter for __ (sperate by space)")
# # for i in num:

# def own_split(num):
#     a= list(num.strip())
#     b=[]
#     c=''
#     for i in a:
#         if i.isnumeric():
#             c+=i     
#         elif i == " ":
#             if c != "":
#                 b.append(int(c))
#                 c=""
#         else: 
#             print("give valid numbers not strings") 
#             break
#     if c != "":
#         b.append(int(c))
#     return b
    
# def highest(l):
#     for i in l:
#         a = 0
#         for j in l:
#             if i>=j:
#                 a+=1
#             if a ==len(l):
#                 return i

# def even(l):
#     b=[]
#     for i in l:
#         if i % 2 == 0:
#             b.append(i)
#     return b

# def threeven(l):
#     b=[]
#     for i in l:
#         if i % 3 == 0:
#             b.append(i)
#     return b

# def pretty_print(l):
#     c=''
#     for i in l:
#        c+=str(i)
#        c+=" "
#     return c.strip()

# last = own_split(num)
# print("Highest number of your given numbers is :",highest(last))
# print("Even numbers of your given numbers is :",pretty_print(even(last)))
# print("Threeven numbers of your given numbers is :",pretty_print(threeven(last)))






# num = input("enter the numbers you wanna enter for __ (sperate by space)")
# def sumstr():
#     a = int()
#     for i in num:
#         a+=int(i)
#     return a
# print(sumstr())






# students = {
#     "Aarav": 87,
#     "Riya": 92,
#     "Karan": 76,
#     "Divya": 88,
#     "Zoya": 91
# }

# def top3(d):
#     b=[]
#     c={}
#     f=0
#     for i in students:
#         b.append(students[i])
#     b.sort()
#     b=b[::-1]
#     for i in range(0,3):
#         for j in students:
#             if students[j] == b[i]:
#                 c[j]=b[i]
#     for i in c:
#         e=["First","Second","Third"]
#         print( i,"is",e[f], "with",c[i],"marks" )
#         f+=1

# top3(students)






# #NUM 2 WORD? HELL YEAH BRAIN DAMAGE
# Scale = {
#     2: "Thousand",
#     3: "Million",
#     4: "Billion",
#     5: "Trillion",
#     6: "Quadrillion",
#     7: "Quintillion",
#     8: "Sextillion",
#     9: "Septillion",
#     10: "Octillion",
#     11: "Nonillion",
#     12: "Decillion"
# }
# damm = {
#     0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
#     5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
#     10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
#     14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
#     18: "Eighteen", 19: "Nineteen", 20: "Twenty", 21: "Twenty-One",
#     22: "Twenty-Two", 23: "Twenty-Three", 24: "Twenty-Four",
#     25: "Twenty-Five", 26: "Twenty-Six", 27: "Twenty-Seven",
#     28: "Twenty-Eight", 29: "Twenty-Nine", 30: "Thirty",
#     31: "Thirty-One", 32: "Thirty-Two", 33: "Thirty-Three",
#     34: "Thirty-Four", 35: "Thirty-Five", 36: "Thirty-Six",
#     37: "Thirty-Seven", 38: "Thirty-Eight", 39: "Thirty-Nine",
#     40: "Forty", 41: "Forty-One", 42: "Forty-Two", 43: "Forty-Three",
#     44: "Forty-Four", 45: "Forty-Five", 46: "Forty-Six",
#     47: "Forty-Seven", 48: "Forty-Eight", 49: "Forty-Nine",
#     50: "Fifty", 51: "Fifty-One", 52: "Fifty-Two", 53: "Fifty-Three",
#     54: "Fifty-Four", 55: "Fifty-Five", 56: "Fifty-Six",
#     57: "Fifty-Seven", 58: "Fifty-Eight", 59: "Fifty-Nine",
#     60: "Sixty", 61: "Sixty-One", 62: "Sixty-Two", 63: "Sixty-Three",
#     64: "Sixty-Four", 65: "Sixty-Five", 66: "Sixty-Six",
#     67: "Sixty-Seven", 68: "Sixty-Eight", 69: "Sixty-Nine",
#     70: "Seventy", 71: "Seventy-One", 72: "Seventy-Two",
#     73: "Seventy-Three", 74: "Seventy-Four", 75: "Seventy-Five",
#     76: "Seventy-Six", 77: "Seventy-Seven", 78: "Seventy-Eight",
#     79: "Seventy-Nine", 80: "Eighty", 81: "Eighty-One",
#     82: "Eighty-Two", 83: "Eighty-Three", 84: "Eighty-Four",
#     85: "Eighty-Five", 86: "Eighty-Six", 87: "Eighty-Seven",
#     88: "Eighty-Eight", 89: "Eighty-Nine", 90: "Ninety",
#     91: "Ninety-One", 92: "Ninety-Two", 93: "Ninety-Three",
#     94: "Ninety-Four", 95: "Ninety-Five", 96: "Ninety-Six",
#     97: "Ninety-Seven", 98: "Ninety-Eight", 99: "Ninety-Nine"
# }

# num = input("Give the Number You wanna turn into Words : ")

# def split3(d):#this will split the number in a list ok to like num = 123456 --> ['123','456']
#     if len(d) % 3 == 1:
#         d = "00"+d
#     elif len(d) % 3 == 2:
#         d = "0" + d
#     b=[]
#     i = len(d)
#     while i>0:
#         b.append(d[i-3:i])
#         i-=3
#     return b[::-1]

# if int(num) != 0:
#     num_list = split3(num) #just running the function
#     semi_final = [] #empty list to just hold values by appending
#     scaling = len(num_list) #using this int as a value to match in the dictionary so like it will specify what scale the number is currently so like 3 = million so it will print one hundred million 
#     for i in num_list:
#         if int(i) % 100 == 0 and int(i) != 0: #checking two cuz if it is 0 it adds zero hundred thousand or whatever
#             ex = i[0]
#             semi_final.append(damm[int(ex)])
#             #above i took the first digit and compared it to dictionary and appended hundred like below
#             semi_final.append("Hundred")

#         elif int(i) in range(1,100): #again gotta remove 0 from being checked will raise error
#             semi_final.append(damm[int(i)])

#         elif int(i) > 100: 
#             #basically combining both above cases
#             semi_final.append(damm[int(i[0])])
#             semi_final.append("Hundred")
#             semi_final.append(damm[int(i[1:])])

#         elif int(i) == 0: #PRETTY IMP why? cuz yk if there is 100,000,069 that 000 is gonna be a problem with scaling
#             scaling -=1

#         if scaling >= 2:
#             #as i said above this one is to print million trillion billion etc
#             semi_final.append(Scale[scaling]+',')
#             scaling-=1

#     if semi_final[-1][-1] == ",": #Preventing if sometime its like one hundred thousand, to not have that comma in the end
#         semi_final[-1] = semi_final[-1].replace(',',"")
#     semi_final.append("Only") #smol lil thing

#     for i in semi_final:
#         print(i,end=" ")
#         #finally printing it all that was in this list lol
#     print("\nThats your number in word form Thanks for Using me YOU LIL BASTARD")
# else: print("WHY ARE YOU ASKING FOR ZERO???? ARE YOU RETARDED YOU FOOL")






# #Matrix CRY :(
# #2x2
# Row1 = input("Enter Row1 : ").split()
# Row2 = input("Enter Row2 : ").split()
# Row3 = input("Enter Row3 : ").split()
# print(Row1)
# print(Row2)
# for i in range(len(Row1)):Row1[i]= int(Row1[i])
# for i in range(len(Row2)):Row2[i]= int(Row2[i])
# for i in range(len(Row3)):Row3[i]= int(Row3[i])

# Column1 = [Row1[0],Row2[0],Row3[0]]
# Column2 = [Row1[1],Row2[1],Row3[1]]
# Column3 = [Row1[2],Row2[2],Row3[2]]

# ResultRow1 = [M1,M2]
# ResultRow2 = [M3,M4]
# print("Here's your desired 2x2 Matrix")
# print(ResultRow1)
# print(ResultRow2)






# # Palindrome checker
# string = input("Enter a string to check if it's a palindrome: ")    
# string = string.lower()  # Convert to lowercase for case-insensitive comparison
# string = string.replace(" ", "")

# i = len(string)-1
# temp = ''
# while i >=0:
#     temp = string[i] + temp
#     i -=1
# if string == temp:
#     print("Yes Given String is a Palindrome")
# else:print("NO")






# #Maths Arithematic mean , Geometric mean , Harmonic mean Not just 2 numbers but for n numbers

# def maininput():
#     num = input("\nOK! Enter ONLY YOUR Number's separated with spaces or comma : ").replace(","," ").split()
#     cleanedlist = []
#     notnum = 0

#     for i in num:
#         try:
#             temp = float(i)
#             if temp.is_integer():
#                 cleanedlist.append(int(i))
#             else:
#                 cleanedlist.append(temp)
#         except ValueError:
#             notnum+=1

#     if notnum > 0:   
#         print(f"I SAID ONLY NUMBERS \nWHAT THE HELL YOU WANT BRUH YOU ENTERED {notnum} NON-NUMERIC STUFF\nSuck it im gonna only count the numeric stuff ig")

#     if cleanedlist == []:
#         print("There isnt even a single number there")
#         return None

#     return cleanedlist

# def AM(l):
#     print("\nProcessing. . . .")
#     sum = 0.0
    
#     for i in l : sum += i

#     answer = float(sum/len(l))
#     print(f"Arithmetic mean of the Numbers\n{l} \nis : {answer}")

# def GM(l):
#     print("\nProcessing. . . .")
#     product = 1
#     negativenum = [i for i in l if i <0]

#     if len(negativenum) % 2 != 0 :
#         print("Undefined because odd number of negative numbers")
#         return 
    
#     for i in l : product *= i
    
#     answer = float((product)**float(1/(len(l))))
#     print(f"Geometric mean of the Numbers\n{l} \nis : {answer}")

# def HM(l):
#     print("\nProcessing. . . .")

#     if 0 in l:
#         print("Undefined Because it contains 0")
#         return 

#     reciprocal_sum = 0.0
#     for i in l : reciprocal_sum += float(1/i)
#     if reciprocal_sum != 0:
#         answer = len(l)/reciprocal_sum  
#         print(f"Harmonic mean of the Numbers\n{l} \nis : {answer}")
#     else:
#         print("The Sum of Reciprocals is near 0 result in a very very large undefined value")

# def Median(l):
#     print("\nProcessing. . . .")
#     if len(l) == 1:
#         print("Atleast give Two values for this one")
#         return
#     count = 0 
#     new = []
#     while l != []:
#         for i in l:
#             for j in l:
#                 if j >= i:
#                     count+=1
#             if count == len(l):
#                 new.append(i)
#                 l.remove(i)
#                 break
#             count = 0
#     temp = len(new)
#     if temp % 2 == 0:
#         answer = (new[temp//2]+new[(temp//2) + 1])//2
#         print(f"Median of the number : {answer}")
#     if temp % 2 != 0:
#         answer = new[temp//2]
#         print(f"Median of the number : {answer} ")

# def Mode(l):
#     print("\nProcessing. . . .")
#     if len(l) == 1:
#         print("Atleast give Two values for this one")
#         return
#     dic = {}
#     count = 0
#     count2 = 0
#     for i in l:
#         if i in dic:
#             continue
#         for j in l:
#             if i == j:
#                 count += 1
#             if count > count2: count2 = count
#         dic[i] = count
#         count = 0
#     print(count2)
#     Mode = [i for i in dic if dic[i]==count2]
#     print(Mode)
#     print(f"Mode : {Mode}")

# samenum = "0"
# cleanedlist = []
# saved = cleanedlist
# Operations = {1:AM,2:GM,3:HM,4:Median,5:Mode}
# while True:

#     choice = int(input("what do you want me to do? \n1. AM\n2. GM\n3. HM\n4. Median\n5. Mode\nYour Selection : "))
#     if choice not in [1,2,3,4,5]:
#         print("\nDo i look like a joke to you? 🤡\nWHY NOT ENTER 1 2 4 5")
#         choice = int(input("Ok this time enter only A NUMBER 1 2 4 5 :"))

#     if samenum == "Y":
#         cleanedlist = saved
#         print('Reusing same numbers. . . .')
#     else:
#         cleanedlist = maininput()
#         saved = cleanedlist

#     if cleanedlist == None:
#         print("Here AM,GM,HM,Median,Mode of nothing vvv \nAM : 0/0\nGM : 0^(1/0)\nHM : 0/(1/0)\nMedian : 0\nMode : 0")
#     else:
#         for i in range(5):Operations[i+1](cleanedlist)

#     again = input("\nDo you wanna go at it again?\n(Y or N) : ").upper()
#     if again != 'Y':
#         print("\n\nThanks for using me! :D\n\n")
#         break
#     elif again == 'Y':
#         samenum = input("Would you like to use the same numbers? : ").upper()
# #What in the fuck am i dooing.... 
# #Improve it like to ask if more than 1 thing is needed by the user like AM and GM






#code and decode text?
# import random

# def random3alpha(alphabet="abcdefghijklmnopqrstuvwxyz"):
#     chars = []
#     for _ in range(3):
#         rand_index = random.randint(0, 25)
#         chars.append(alphabet[rand_index])
#     return "".join(chars)

# def code(text):
#     if len(text) >= 3:
#         text = text[1:] + text[0]   # rotate left
#         prefix, suffix = random3alpha(), random3alpha()
#         return prefix + text + suffix
#     else:
#         return text[::-1]

# def decode(text):
#     if len(text) >= 3:
#         text = text[3:-3]           # remove padding
#         return text[-1] + text[:-1] # rotate right
#     else:
#         return text[::-1]

# while True:
#     action = input("Would you like to decode or code: ").strip().lower()
#     if action == "code":
#         text = input("Enter your string to Code: ").strip()
#         print(code(text))
#     else:
#         text = input("Enter your Code to Decode: ").strip()
#         print(decode(text))
    
#     again = input("Would you like to go again? ").strip().lower()
#     if again != "yes":
#         print("Good use of me")
#         break




#Roman Numeral Converter
#    * Convert integers to Roman numerals
#    * Input: 2025 → Output: MMXXV
#    * Try building your own logic without `.roman` modules

