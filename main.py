f=open('space.txt',encoding='UTF8').read()
f=f.split('\n')
a=[]
for i in f:
    a.append(i.split('*'))
#Задание 1
f=open("space_new.txt","w",encoding='UTF8')
for el in a:
   if el[2]=='0 0':
       xd, yd= el[3].split()
       code, number= el[0].split('-')
       n=int(number[0])
       m=int(number[1])
       t=len(el[1])
       if n>5:
           x=n+int(xd)
       else:
           x=-(n+int(xd))*4+t
       if m > 3:
           y = m + t + int(yd)
       else:
           y = -(n + int(yd))*m
       el[2]=str(x)+' '+str(y)
       if code[-1]=='V':
           f.write('<'+code+'> - (<'+str(x)+'>, <'+str(y)+'>)')

#Задание 2

def getNumber(name):
    code, number= name.split('-')
    return number
for i in range(1,len(a)):
    x=a[i]
    j=i
    while j>0 and float(getNumber(a[j - 1][0])) > float(getNumber(x[0])):
        a[j] = a[j - 1]
        j-=1
    a[j]=x
b=a[:10]
for el in b:
    print(el[0])






