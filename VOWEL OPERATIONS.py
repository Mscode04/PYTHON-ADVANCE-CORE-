list1=[]
list2=[]
x=input("enter the string ypou want to remove the vowels:  ")
i=0
l=0
for ch in x:
    if ch in "aeiouAEIOU":
        i=i+1
        list1.append(ch)
    else:
        l=l+1
        list2.append(ch)
print("number of vowel is=  ",i,"  and the vowels is=  ",list1)        
print("number of consonence is=  ",l,"  and the consonence  is=  ",list2)
