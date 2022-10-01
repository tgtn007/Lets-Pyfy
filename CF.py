T=lambda : range(int(input()))
A=lambda : list(map(int,input().split()))
isodd=lambda a : a&1
for _ in T() :
    a=A()
    r,g,b,w=a
    if r==0 or g==0 or b==0:
        x=0
        if isodd(r) :
            x=x+1
        if isodd(g) :
            x=x+1
        if isodd(b) :
            x=x+1

        if x==2 :
            print("No")
        elif x==1 :
            if isodd(w) :
                print("No")
            else :
                print("Yes")
        else :
            print("Yes")
    else :
        x=0
        if isodd(r) :
            x=x+1
        if isodd(g) :
            x=x+1
        if isodd(b) :
            x=x+1

        if x==3 or x==0:
            print("Yes")
        elif x==2 :
            if isodd(w) :
                print("Yes")
            else :
                print("No")
        else :
            if isodd(w) :
                print("No")
            else :
                print("Yes")



