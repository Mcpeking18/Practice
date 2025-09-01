#NUM 2 WORD? HELL YEAH BRAIN DAMAGE
Scale = {
    2: "Thousand",
    3: "Million",
    4: "Billion",
    5: "Trillion",
    6: "Quadrillion",
    7: "Quintillion",
    8: "Sextillion",
    9: "Septillion",
    10: "Octillion",
    11: "Nonillion",
    12: "Decillion"
}
damm = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
    18: "Eighteen", 19: "Nineteen", 20: "Twenty", 21: "Twenty-One",
    22: "Twenty-Two", 23: "Twenty-Three", 24: "Twenty-Four",
    25: "Twenty-Five", 26: "Twenty-Six", 27: "Twenty-Seven",
    28: "Twenty-Eight", 29: "Twenty-Nine", 30: "Thirty",
    31: "Thirty-One", 32: "Thirty-Two", 33: "Thirty-Three",
    34: "Thirty-Four", 35: "Thirty-Five", 36: "Thirty-Six",
    37: "Thirty-Seven", 38: "Thirty-Eight", 39: "Thirty-Nine",
    40: "Forty", 41: "Forty-One", 42: "Forty-Two", 43: "Forty-Three",
    44: "Forty-Four", 45: "Forty-Five", 46: "Forty-Six",
    47: "Forty-Seven", 48: "Forty-Eight", 49: "Forty-Nine",
    50: "Fifty", 51: "Fifty-One", 52: "Fifty-Two", 53: "Fifty-Three",
    54: "Fifty-Four", 55: "Fifty-Five", 56: "Fifty-Six",
    57: "Fifty-Seven", 58: "Fifty-Eight", 59: "Fifty-Nine",
    60: "Sixty", 61: "Sixty-One", 62: "Sixty-Two", 63: "Sixty-Three",
    64: "Sixty-Four", 65: "Sixty-Five", 66: "Sixty-Six",
    67: "Sixty-Seven", 68: "Sixty-Eight", 69: "Sixty-Nine",
    70: "Seventy", 71: "Seventy-One", 72: "Seventy-Two",
    73: "Seventy-Three", 74: "Seventy-Four", 75: "Seventy-Five",
    76: "Seventy-Six", 77: "Seventy-Seven", 78: "Seventy-Eight",
    79: "Seventy-Nine", 80: "Eighty", 81: "Eighty-One",
    82: "Eighty-Two", 83: "Eighty-Three", 84: "Eighty-Four",
    85: "Eighty-Five", 86: "Eighty-Six", 87: "Eighty-Seven",
    88: "Eighty-Eight", 89: "Eighty-Nine", 90: "Ninety",
    91: "Ninety-One", 92: "Ninety-Two", 93: "Ninety-Three",
    94: "Ninety-Four", 95: "Ninety-Five", 96: "Ninety-Six",
    97: "Ninety-Seven", 98: "Ninety-Eight", 99: "Ninety-Nine"
}

num = input("Give the Number You wanna turn into Words : ")

def split3(d):#this will split the number in a list ok to like num = 123456 --> ['123','456']
    if len(d) % 3 == 1:
        d = "00"+d
    elif len(d) % 3 == 2:
        d = "0" + d
    b=[]
    i = len(d)
    while i>0:
        b.append(d[i-3:i])
        i-=3
    return b[::-1]

if int(num) != 0:
    num_list = split3(num) #just running the function
    semi_final = [] #empty list to just hold values by appending
    scaling = len(num_list) #using this int as a value to match in the dictionary so like it will specify what scale the number is currently so like 3 = million so it will print one hundred million 
    for i in num_list:
        if int(i) % 100 == 0 and int(i) != 0: #checking two cuz if it is 0 it adds zero hundred thousand or whatever
            ex = i[0]
            semi_final.append(damm[int(ex)])
            #above i took the first digit and compared it to dictionary and appended hundred like below
            semi_final.append("Hundred")

        elif int(i) in range(1,100): #again gotta remove 0 from being checked will raise error
            semi_final.append(damm[int(i)])

        elif int(i) > 100: 
            #basically combining both above cases
            semi_final.append(damm[int(i[0])])
            semi_final.append("Hundred")
            semi_final.append(damm[int(i[1:])])

        elif int(i) == 0: #PRETTY IMP why? cuz yk if there is 100,000,069 that 000 is gonna be a problem with scaling
            scaling -=1

        if scaling >= 2:
            #as i said above this one is to print million trillion billion etc
            semi_final.append(Scale[scaling]+',')
            scaling-=1

    if semi_final[-1][-1] == ",": #Preventing if sometime its like one hundred thousand, to not have that comma in the end
        semi_final[-1] = semi_final[-1].replace(',',"")
    semi_final.append("Only") #smol lil thing

    for i in semi_final:
        print(i,end=" ")
        #finally printing it all that was in this list lol
    print("\nThats your number in word form Thanks for Using me YOU LIL BASTARD")
else: print("WHY ARE YOU ASKING FOR ZERO???? ARE YOU RETARDED YOU FOOL")