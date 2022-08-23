try:
    t=int(input())
    for i in range(t):
        f,l=map(int,input().split())
        c=1 
        k=0
        a=0
        for j in range(l):
             k=k*10+c 
             if c>=f and c<=l and k%3==0:
                 a=a+1
             c+=1
        print(f'Case {i+1}: {a}')
except:
    pass
