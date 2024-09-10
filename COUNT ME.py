def writef():
    L=["Will you give me a cup of tea?\n","you and me are good pairs\n","What did you want me to say?\n","jakeb is my father"]
    f2.writelines(L)
def countp():
    count=0
    f2.seek(0)
    l=f2.read()
    for i in l.split():
        if i== "me":
            count+=1
    print(count)            
with open("poem.txt","w+") as f2:
    writef()
    countp()
