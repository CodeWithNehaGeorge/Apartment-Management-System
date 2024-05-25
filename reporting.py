import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()

def  TotalDues():
   cur.execute("SELECT SUM(AMOUNT_PAID) FROM MAINTENANCE_FEE")
   s1=cur.fetchone()
   print("\nTOTAL DUES")
   print("______________")
   print("\n",s1[0])


def CollectedAmount():
   cur.execute("SELECT SUM(AMOUNT_DUE) FROM MAINTENANCE_FEE")
   s2=cur.fetchone()
   print("\nTOTAL COLLECTED AMOUNT")
   print("________________________________")
   print("\n",s2[0])


def mainreporting():
   while True:
      print("\n1.TO VIEW TOTAL DUES")
      print("2.TO VIEW TOTAL COLLECTED AMOUNT")
      print("3.EXIT")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         TotalDues()
      elif ch==2:
         CollectedAmount()
      elif ch==3:
         mycon.close()
         break
      else:
         print("INVALID CHOICE")

   
   
   
