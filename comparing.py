def maininput() -> list[float]:
    num = input("\nOK! Enter ONLY YOUR Number's separated with spaces or comma : ").replace(",", " ").split()
    cleaned_list = []
    notnum = 0

    for i in num:
        try:
            temp = float(i)
            cleaned_list.append(temp if not temp.is_integer() else int(i))
        except ValueError:
            notnum += 1

    if notnum > 0:   
        print(f"I SAID ONLY NUMBERS \nWHAT THE HELL YOU WANT BRUH YOU ENTERED {notnum} NON-NUMERIC STUFF\nSuck it im gonna only count the numeric stuff ig")

    if cleaned_list == []:
        print("There isnt even a single number there")
        return None

    return cleaned_list


def AM(l):
    print("\nProcessing. . . .")
    total = 0
    count = 0
    for i in l:
        total += i
        count += 1
    if count == 0:
        answer = 0
    else:
        answer = total / count
    print(f"Arithmetic mean of the Numbers {l} \nis : {answer}")


def GM(l):
    print("\nProcessing. . . .")
    product = 1
    count = 0
    negativenum = [i for i in l if i < 0]

    if len(negativenum) % 2 != 0:
        print("Undefined because odd number of negative numbers")
        return
    
    for i in l:
        product *= i
        count += 1

    answer = product ** (1 / count)
    print(f"Geometric mean of the Numbers {l} \nis : {answer}")


def HM(l):
    print("\nProcessing. . . .")
    if 0 in l:
        print("Undefined Because it contains 0")
        return 

    reciprocal_sum = 0.0
    for i in l:
        reciprocal_sum += 1 / i
    if reciprocal_sum != 0:
        answer = len(l) / reciprocal_sum  
        print(f"Harmonic mean of the Numbers {l} \nis : {answer}")
    else:
        print("The Sum of Reciprocals is near 0 result in a very very large undefined value")


def Median(l):
    print("\nProcessing. . . .")
    if len(l) == 1:
        print("Atleast give Two values for this one dumbass")
        return

    # manual sort
    arr = l[:]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    temp = len(arr)
    if temp % 2 == 0:
        answer = (arr[temp//2 - 1] + arr[temp//2]) / 2
    else:
        answer = arr[temp//2]
    print(f"Median of the number : {answer}")


def Mode(l):
    print("\nProcessing. . . .")
    if len(l) == 1:
        print("Atleast give Two values for this one bruh")
        return

    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    max_count = 0
    for val in dic.values():
        if val > max_count:
            max_count = val

    mode = [i for i in dic if dic[i] == max_count]
    print(f"Mode : {mode}")


samenum = "0"
cleanedlist = []
Operations = {1: AM, 2: GM, 3: HM, 4: Median, 5: Mode}

while True:
    while True:
        try:
            choice = int(input("What do you want me to do? \n1. AM\n2. GM\n3. HM\n4. Median\n5. Mode\nYour Selection : "))
            if choice in [1, 2, 3, 4, 5]:
                saved = maininput()
                if saved:
                    Operations[choice](saved)
                break  # valid choice, exit loop
            else:
                print("\nDo I look like a joke to you? 🤡\nWHY NOT ENTER 1 2 3 4 5")
        except ValueError:
            print("Ok this time enter only A NUMBER 1 2 3 4 5 :")

    again = input("\nDo you wanna go at it again?\n(Y or N) : ").upper()
    if again != 'Y':
        print("\n\nThanks for using me! :D\n\n")
        break
    elif again == 'Y':
        samenum = input("Would you like to use the same numbers? : ").upper()

    if samenum == "0":
        pass
    elif samenum == "Y":
        cleanedlist = saved
        print('Reusing same numbers. . . .')
    else:
        cleanedlist = maininput()

    if cleanedlist == [] or cleanedlist is None:
        print("Here AM,GM,HM,Median,Mode of nothing vvv \nAM : 0/0\nGM : 0^(1/0)\nHM : 0/(1/0)\nMedian : 0\nMode : 0")
    else:
        for i in range(5):
            Operations[i+1](cleanedlist)
