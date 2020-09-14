Coup_one=int(input())
Coup_two=int(input())
Turn1=1
Turn2=0
while Coup_one!=0 or Coup_two!=0:
    if Turn1>Turn2:
        if Coup_one==Coup_two:
            Coup_two-=1
        else:
            Coup_one+=1
            Coup_two-=1
    else:
        if Coup_one==Coup_two:
            Coup_one-=1
        else:
            Coup_two+=1
            Coup_one-=1
    if Turn1>Turn2:
        Turn2+=1
    else:
        Turn1+=1
if Coup_one==0:
     print('победил 2-ой игрок')
elif Coup_two==0:
     print('победил 1-ый игрок')