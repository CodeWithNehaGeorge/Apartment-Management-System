import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()

def addresidentinfo():
   create="CREATE TABLE IF NOT EXISTS RESIDENTMANAGEMENT(RESIDENT_ID INT PRIMARY KEY,RESIDENT_NAME VARCHAR(20),FLAT_NUMBER VARCHAR(6),CONTACT_NUMBER VARCHAR(20),EMAIL_ID VARCHAR(50))"
   cur.execute(create)
   ch="Y"
   while ch in "yY":
      resid=int(input("\nENTER THE RESIDENT ID:"))
      name=input("ENTER THE NAME:")
      flatno=input("ENTER THE FLAT NUMBER:")
      phoneno=input("ENTER CONTACT NUMBER:")
      email=input("ENTER EMAIL ADDRESS:")
      query="INSERT INTO RESIDENTMANAGEMENT VALUES({},'{}','{}','{}','{}')".format(resid,name,flatno,phoneno,email)
      cur.execute(query)
      mycon.commit()
      ch=input("\nDO YOU WANT TO ADD MORE?(Y/N):")
   
      
def updateresidentinfo():
   resid=int(input("\nENTER THE RESIDENT_ID TO BE UPDATED:"))
   query="SELECT * FROM RESIDENTMANAGEMENT WHERE RESIDENT_ID={}".format(resid)
   cur.execute(query)
   data=cur.fetchone()
   if data==None:
      print("RECORD NOT FOUND TRY AGAIN")
   else:
      print("\nMENU")
      print('________')
      print("\nENTER 1 FOR UPDATING ALL RESIDENT INFORMATION")
      print("ENTER 2 FOR UPDATING  RESIDENT_NAME")
      print("ENTER 3 FOR UPDATING  FLAT_NUMBER")
      print("ENTER 4 FOR UPDATING CONTACT_NUMBER")
      print("ENTER 5 FOR UPDATING EMAIL_ID")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         name=input("\nENTER THE NAME:")
         flatno=input("ENTER THE FLAT NUMBER:")
         phoneno=input("ENTER CONTACT NUMBER:")
         email=input("ENTER EMAIL ADDRESS:")
         query="UPDATE RESIDENTMANAGEMENT SET RESIDENT_NAME='{}',FLAT_NUMBER='{}',CONTACT_NUMBER='{}',EMAIL_ID='{}' WHERE RESIDENT_ID='{}'".format(name,flatno,phoneno,email,resid)
         cur.execute(query)
         mycon.commit()
         print("\nALL RESIDENT DETAILS UPDATED")
      elif ch==2:
         name=input("\nENTER THE NAME :")
         query="UPDATE RESIDENTMANAGEMENT SET RESIDENT_NAME='{}' WHERE RESIDENT_ID={}".format(name,resid)
         cur.execute(query)
         mycon.commit()
         print("\nRESIDENT_ID UPDATED")
      elif ch==3:
         flatno=input("\nENTER THE FLAT NUMBER :")
         query="UPDATE RESIDENTMANAGEMENT SET FLAT_NUMBER='{}' WHERE RESIDENT_ID={}".format(flatno,resid)
         cur.execute(query)
         mycon.commit()
         print("\nFLAT_NUMBER UPDATED")
      elif ch==4:
         phoneno=int(input("\nENTER CONTACT NUMBER :"))
         query="UPDATE RESIDENTMANAGEMENT SET CONTACT_NUMBER={} WHERE RESIDENT_ID={}".format(phoneno,resid)
         cur.execute(query)
         mycon.commit()
         print("\nCONTACT_NUMBER UPDATED")
      elif ch==5:
         email=input("\nENTER EMAIL ADDRESS :")
         query="UPDATE RESIDENTMANAGEMENT SET EMAIL_ID='{}' WHERE RESIDENT_ID={}".format(email,resid)
         cur.execute(query)
         mycon.commit()
         print("\nEMAIL_ID UPDATED")
      else:
            print("\nINVALID INPUT")
         
def deleteresidentinfo():
   resid=int(input("\nENTER THE RESIDENT ID TO BE DELETED:"))
   query="DELETE FROM RESIDENTMANAGEMENT WHERE RESIDENT_ID={}".format(resid)
   cur.execute(query)
   rec=cur.rowcount
   if rec==0:
      print("RECORD NOT FOUND")
   else:
      print("\nRECORD DELETED")
   mycon.commit()


def displayresideninfo():
   cur.execute("SELECT * FROM RESIDENTMANAGEMENT")
   records=cur.fetchall()
   print("\nRESIDENT INFORMATION")
   print("____________________________")
   print("\nRESIDENT_ID\t\tRESIDENT_NAME\t\t\tFLAT_NUMBER\t\tCONTACT_NUMBER\t\tEMAIL_ID")  
   for row in records:
        print("\n",row[0],"\t\t\t",row[1].ljust(15),"\t\t\t",row[2].ljust(10),"\t\t\t",row[3].ljust(10),"\t\t\t",row[4].ljust(10))



def mainresident():
   while True:
      print("\n1.TO ADD RESIDENT INFORMATION")
      print("2.TO UPDATE RESIDENT INFORMATION")
      print("3.TO DELETE RESIDENT INFORMATION")
      print("4.TO DISPLAY RESIDENT INFORMATION")
      print("5.EXIT")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         addresidentinfo()
      elif ch==2:
         updateresidentinfo()
      elif ch==3:
         deleteresidentinfo()
      elif ch==4:
         displayresideninfo()
      elif ch==5:
         mycon.close()
         break
      else:
         print("INVALID CHOICE")













               
               
               
               
               
               
               
   
            
            
         
            
            
            
            
            
            
            
      


      
   
