#import sys
#sys.stdin = open('input.txt', "r")
#sys.stdout = open('output.txt', "w")
#Coup_one, Coup_two=map(int, input().split())
Coup_one=int(input())
Coup_two=int(input())
Maksim=1
Dima=0 #1
while Coup_one!=0 and Coup_two!=0:
    if Maksim>Dima:
        if Coup_one==Coup_two:
            Coup_two-=1 #1,
        else:
            Coup_one-=1
            Coup_two-=1
    else:
        if Coup_one==Coup_two:
            Coup_one-=1
        else:
            Coup_two-=1 #2
            Coup_one-=1 #1
    if Maksim>Dima:
        Dima+=1
    else:
        Maksim+=1
if Coup_one==0:
     print('1')
elif Coup_two==0:
     print('2')