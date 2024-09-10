x=input("enter the string ypou want to remove the vowels:  ")
n=" "
for ch in x:
    if ch in "aeiouAEIOU":
        n=n+"$"
    else:
        n=n+ch
print(n)        
