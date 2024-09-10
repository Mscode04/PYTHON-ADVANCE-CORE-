import os
def filecopy(x1,y1):
      file1=open(x1,'r')
      file2=open(y1,'w')
      line=file1.readline()
      while line!="" :
            file2.write(line)
            line=file1.readline()
      file1.close()       
      file2.close()
def main():
    x=input("enter the file1path:   ")
    y=input("enter the file2path:   ")
    filecopy(x,y)
main()
print("FINISH COPING TO ONE FILE TO OTHER")

