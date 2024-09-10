import mysql.connector as x
db = x.connect(host = "localhost",user = "root",passwd = "admin",database = "shahenxylem")
c=db.cursor()
def deldata():
      query = ("delete from student where rno=32")
      c.execute(query)
      print("record deleted")
      db.commit()
deldata()


          
      



            
