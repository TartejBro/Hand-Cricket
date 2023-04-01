import random
print("Choose any number between 1 to 6")
lst=[1,2,3,4,5,6]
score_user=0
score_comp=0
i=0
print("You are batting")
while i<=35:
    input_user=int(input("Enter Input:"))
    input_comp=random.choice(lst)
    i=i+1
    if input_user==input_comp:
        print("Computer Selected:",input_comp)
        print("You are Out")
        print("Total User Score=",score_user)
        i=40
    else:
        print("Computer Selected:",input_comp)
        print("You scored",input_user)
        score_user=score_user+input_user
        print("Total User Score=",score_user)
print("You are bowling")
i=0
while i<=35:
    input_user=int(input("Enter Input:"))
    input_comp=random.choice(lst)
    i=i+1
    if input_user==input_comp:
        print("Computer Selected:",input_comp)
        print("Computer Is Out")
        print("Total Computer Score=",score_comp)
        i=40
    else:
        print("Computer Selected:",input_comp)
        print("Computer scored",input_comp)
        score_comp=score_comp+input_comp
        print("Total Computer Score=",score_comp)
res1=score_user-score_comp
res2=score_comp-score_user
if score_user>score_comp:
    print("You won by ",res1," runs")
elif score_user==score_comp:
    print("Match Tied")
else:
    print("You Lost by", res2,"runs")
        

        
        
