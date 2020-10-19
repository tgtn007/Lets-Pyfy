def similar(A,N):
    p=0
    count=0
    for i in range(len(minimum(A))):
        c=[]
        for j in range(N):
            c.append(A[j][i])
        if c==[A[0][i]]*N and p==0:
            count=count+1
        else:
            p=1
    for k in range(count):
        print(A[0][k],end='')

def minimum(A):
    E=[]
    for ele in A:
        E.append(len(ele))
    x=A[E.index(min(E))]
    return x

N=int(input())
A=[]
for i in range(N):
    A.append(input())
similar(A,N)
