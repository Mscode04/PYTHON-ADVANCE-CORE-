x=open('f1.txt','r')
y=open('f2.txt','w')   
for i in x:
    y.write(i)
x.close()
y.close()
