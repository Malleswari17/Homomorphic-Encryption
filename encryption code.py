s=list(input())
t=""
n1=1 
n2=1
for i in range(len(s)):
    np=0
    ntg=0
    np=int((n1*(n1+1)*(n1+2))/6)
    x=ord(s[i])
    y=(x^np)
    ntg=int((n2*(n2+1)*(n2+2)*(n2+3))/24)
    f=y//ntg
    r=y%ntg
    t=t+'f'+str(f)+'r'+str(r)
    n1=n1+1
    n2=n2+1
print(t)

