T=int(input())
for i in range(T) :
    N=int(input())
    if N==44 :
        print('YES')
        print(6,10,15,13)
    elif N==40 :
        print('YES')
        print(6,10,15,9)
    elif N==36 :
        print('YES')
        print(6,10,15,5)
    elif N>30 :
        
        print('YES')
        print(6,10,14,N-30)
    else :
        print('NO')