import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()


def addflatdetails():
    create="create table if not exists FLAT(FLAT_NUMBER VARCHAR(20) PRIMARY KEY,FLOOR INT,AREA INT,TYPE VARCHAR(20),OWNER_STATUS VARCHAR(20),MAINTENANCE_FEE INT)"
    cur.execute(create)
    ch='Y'
    while ch in 'yY':
           fn=input("\nENTER THE FLAT NUMBER:")
           fl=int(input("ENTER THE FLOOR NUMBER:"))
           ar=int(input("ENTER THE AREA(SQ.FEET):"))
           ty=input("ENTER THE TYPE:")
           os=input("ENTER OWNER STATUS(TENANT/OWNER):")
           mf=int(input("ENTER THE MAINTENANCE FEE:"))
           query="INSERT INTO FLAT VALUE('{}',{},{},'{}','{}',{})".format(fn,fl,ar,ty,os,mf)
           cur.execute(query)
           mycon.commit()
           ch=input("\nDO YOU WANT TO ADD MORE?(Y/N)")


def updateflatdetails():
      fn=input("\nENTER THE FLAT NUMBER TO BE UPDATED:")
      query="SELECT * FROM FLAT WHERE FLAT_NUMBER='{}'".format(fn)
      cur.execute(query)
      data=cur.fetchone()
      if data==None:
               print("RECORD NOT FOUND TRY AGAIN")
      else:
         print("\nMENU")
         print("________")
         print("\nENTER 1 FOR UPDATING ALL FLAT DETAILS")
         print("ENTER 2 FOR UPDATING OWNER STATUS")
         print("ENTER 3 FOR UPDATING MAINTENANCE FEE")
         ch=int(input("\nENTER YOUR CHOICE:"))
         if ch==1:
            os=input("\nENTER THE OWNER STATUS(TENANT/OWNER):")
            mf=int(input("ENTER MAINTENANCE FEE:"))
            query="UPDATE FLAT SET OWNER_STATUS='{}',MAINTENANCE_FEE={} WHERE FLAT_NUMBER='{}'".format(os,mf,fn)
            cur.execute(query)
            mycon.commit()
            print("\nALL FLAT DETAILS UPDATED")
         elif ch==2:
            os=input("\nENTER THE OWNER STATUS(TENANT/OWNER):")
            query="UPDATE FLAT SET OWNER_STATUS='{}' WHERE FLAT_NUMBER='{}'".format(os,fn)
            cur.execute(query)
            mycon.commit()
            print("\nOWNER STAUS UPDATED")
         elif ch==3:
            mf=int(input("\nENTER THE MAINTENANCE FEE:"))
            query="UPDATE FLAT SET MAINTENANCE_FEE={} WHERE FLAT_NUMBER='{}'".format(mf,fn)
            cur.execute(query)
            mycon.commit()
            print("\nMAINTENANCE FEE UPDATED")
         else:
             print("\nINVALID INPUT")


def deleteflatdetails():
   fn=input("\nENTER THE FLAT NUMBER TO BE DELETED:")
   query="DELETE FROM FLAT WHERE FLAT_NUMBER='{}'".format(fn)
   cur.execute(query)
   rec=cur.rowcount
   if rec==0:
      print("RECORD NOT FOUND")
   else:
      print("\nRECORD DELETED")
   mycon.commit()


def displayflatdetails():
   cur.execute("SELECT * FROM FLAT")
   record=cur.fetchall()
   print("\nFLAT INFORMATION")
   print("______________________")
   print("\nFLAT NUMBER\t\tFLOOR\t\tAREA\t\tTYPE\t\tOWNER STATUS\t\tMAINTENANCE FEE")
   for row in record:
      print("\n",row[0],"\t\t\t",row[1],"\t\t",row[2],"\t\t",row[3].ljust(10),"\t\t",row[4].ljust(10),"\t\t",row[5])


def mainflat():
   while True:
      print("\n1.TO ADD FLAT DETAILS")
      print("2.TO UPDATE FLAT DETAILS")
      print("3.TO DELETE FLAT DETAILS")
      print("4.TO DISPLAY FLAT DETAILS")
      print("5.EXIT")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         addflatdetails()
      elif ch==2:
         updateflatdetails()
      elif ch==3:
         deleteflatdetails()
      elif ch==4:
         displayflatdetails()
      elif ch==5:
         mycon.close()
         break
      else:
         print("INVALID CHOICE")
      








         
         
      

