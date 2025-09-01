# grade calculator
# ??
Sub1 = ['Physics','Chemistry','Maths','Computer Science', 'English']
Sub2 = ['Physics','Chemistry','Maths','Biology', 'English']
Sub3 = ['Physics','Chemistry','Hindi','Biology', 'English']

print( "What subject do you study? Select from below \nPCM" , Sub1 , "\nPCMB" ,Sub2 , "\nPCB" , Sub3 ,"\nEnter 1 2 3 respectively to select your subect")
Class = int(input())
print()
dict = {}

def total(sub):
    totally = 0
    for i in range(len(sub)):
        print(f"Please enter your marks in {sub[i]}" ,end = " : ")
        a = float(input())
        if a <= 33:
            dict[sub[i]] = "FAILED"
        else:
            dict[sub[i]] = "PASSED!!!!"
        totally = totally + a
    return (totally/5)

def ask_sub(Class):
    # if Class == 1:
    #     a = total(Sub1)
    # elif Class == 2:
    #     a = total(Sub2)
    # else:
    #     a = total(Sub3)
    a = total(Sub1) if Class == 1 else total(Sub2) if Class == 2 else total(Sub3) 
    #TURNS OUT YOU CAN WRITE IT THIS WAY WHAT THE FUCK??????
    return a

marks = ask_sub(Class)
print("\nYour final average marks are : ", marks, "\n")

# I'd hope this below can be written like that 
if marks >= 90:
    print("Your final grade is A\n")
elif marks >= 80:
    print("Your final grade is B\n")
elif marks >= 70:
    print("Your final grade is C\n")
elif marks >= 60:
    print("Your final grade is D\n")
else:
    print("I would quit studying atp\n") 

# CRAZY shit even tho its not that good to write like that but dammmm
# print("Your final grade is A\n") if marks >= 90 else print("Your final grade is B\n") if marks >= 80 else print("Your final grade is C\n") if marks >= 70 else print("Your final grade is D\n") if marks >= 60 else print("I would quit studying atp\n")

print("About your subjects : \n")
for i in dict:
    print(i + " : " + dict[i])

# if subject not present
# ask the people their subjects