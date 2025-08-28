#Maths Arithematic mean , Geometric mean , Harmonic mean, Median, Mode Not just 2 numbers but for n numbers
#Mood changed now im gonna write all of the maths functions i know here

def maininput():
    num = input("\nOK! Enter ONLY YOUR Number's separated with spaces or comma : ").replace(","," ").split()
    cleaned_list = []
    notnum = 0

    for i in num:
        try:
            temp = float(i)
            if temp.is_integer():
                cleaned_list.append(int(i))
            else:
                cleaned_list.append(temp)
        except ValueError:
            notnum+=1

    if notnum > 0:   
        print(f"I SAID ONLY NUMBERS \nWHAT THE HELL YOU WANT BRUH YOU ENTERED {notnum} NON-NUMERIC STUFF\nSuck it im gonna only count the numeric stuff ig")

    if cleaned_list == []:
        print("There isnt even a single number there")
        return None

    return cleaned_list

def AM(l):
    print("\nProcessing. . . .")
    sum = 0.0
    for i in l : sum += i
    if l == None:answer = 0
    else:answer = float(sum/len(l))
    print(f"Arithmetic mean of the Numbers\n{l} \nis : {answer}")

def GM(l):
    print("\nProcessing. . . .")
    product = 1
    negativenum = [i for i in l if i <0]

    if len(negativenum) % 2 != 0 :
        print("Undefined because odd number of negative numbers")
        return 
    
    for i in l : product *= i
    
    answer = float((product)**float(1/(len(l))))
    print(f"Geometric mean of the Numbers\n{l} \nis : {answer}")

def HM(l):
    print("\nProcessing. . . .")

    if 0 in l:
        print("Undefined Because it contains 0")
        return 

    reciprocal_sum = 0.0
    for i in l : reciprocal_sum += float(1/i)
    if reciprocal_sum != 0:
        answer = len(l)/reciprocal_sum  
        print(f"Harmonic mean of the Numbers\n{l} \nis : {answer}")
    else:
        print("The Sum of Reciprocals is near 0 result in a very very large undefined value")

def Median(l):
    print("\nProcessing. . . .")
    if len(l) == 1:
        print("Atleast give Two values for this one")
        return
    count = 0 
    new = []
    while l != []:
        for i in l:
            for j in l:
                if j >= i:
                    count+=1
            if count == len(l):
                new.append(i)
                l.remove(i)
                break
            count = 0
    temp = len(new)
    if temp % 2 == 0:
        answer = (new[temp//2]+new[(temp//2) + 1])//2
        print(f"Median of the number : {answer}")
    if temp % 2 != 0:
        answer = new[temp//2]
        print(f"Median of the number : {answer} ")

def Mode(l):
    print("\nProcessing. . . .")
    if len(l) == 1:
        print("Atleast give Two values for this one")
        return
    dic = {}
    count = 0
    count2 = 0
    for i in l:
        if i in dic:
            continue
        for j in l:
            if i == j:
                count += 1
            if count > count2: count2 = count
        dic[i] = count
        count = 0
    print(count2)
    Mode = [i for i in dic if dic[i]==count2]
    print(Mode)
    print(f"Mode : {Mode}")

samenum = "0"
cleanedlist = []
saved = cleanedlist
Operations = {1:AM,2:GM,3:HM,4:Median,5:Mode}
while True:

    while True:
        try:
            choice = int(input("What do you want me to do? \n1. AM\n2. GM\n3. HM\n4. Median\n5. Mode\nYour Selection : "))
            if choice in [1, 2, 3, 4, 5]:
                Operations[choice](maininput())
                break  # valid choice, exit loop
            else:
                print("\nDo I look like a joke to you? 🤡\nWHY NOT ENTER 1 2 3 4 5")
        except ValueError as e:
            print("Ok this time enter only A NUMBER 1 2 3 4 5 :")

    if samenum == "0":
        pass
    elif samenum == "Y":
        cleanedlist = saved
        print('Reusing same numbers. . . .')
    else:
        cleanedlist = maininput()
        saved = cleanedlist

    if cleanedlist == None:
        print("Here AM,GM,HM,Median,Mode of nothing vvv \nAM : 0/0\nGM : 0^(1/0)\nHM : 0/(1/0)\nMedian : 0\nMode : 0")
    else:
        for i in range(5):
            Operations[i+1](cleanedlist)

    again = input("\nDo you wanna go at it again?\n(Y or N) : ").upper()
    if again != 'Y':
        print("\n\nThanks for using me! :D\n\n")
        break
    elif again == 'Y':
        samenum = input("Would you like to use the same numbers? : ").upper()

#What in the fuck am i dooing.... 
#Improve it like to ask if more than 1 thing is needed by the user like AM and GM