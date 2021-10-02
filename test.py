import time
x=int(input("Enter the no="))
start=time.time()
for i in range(2,(10**x)+1):
    if i==2:
        print(2)
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
print(time.time()-start)