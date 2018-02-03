l=[]
d={}
for i in range(1,51):
  d[i]=input()
from operator import itemgetter
m=sorted(d.items(), key=itemgetter(1))
#print(m)
for j in range(0,50):
   if m[j][1]!='-1':
     l.append(m[j][0])
for k in range(len(l)-1,-1,-1):
  f=open(""+str(l[k])+".txt","r")
  print(str(l[k]),end='')
  print(" Title : ",end='')
  while True:
      c = f.read(1)
      if not c:
        break
      elif c!='\n' :
        print(c, end='')
      elif c=='\n':
        print('\n')
        break

