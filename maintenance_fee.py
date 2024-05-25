import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()

def AddMaintenance():
    table=("CREATE TABLE IF NOT EXISTS MAINTENANCE_FEE(RECEIPT_ID INT NOT NULL PRIMARY KEY,FLAT_NUMBER VARCHAR(5) NOT NULL,MONTH VARCHAR(10),AMOUNT_PAID INT,AMOUNT_DUE INT)")
    cur.execute(table)
    ch="Y"
    while ch in "Yy":
        rec_id=int(input("\nENTER THE RECEIPT ID:"))
        flat_no=input("ENTER THE FLAT NUMBER:")
        month=input("ENTER THE MONTH FOR MAINTENANCE:")
        amt_paid=int(input("ENTER THE AMOUNT PAID:"))
        amt_due=int(input("ENTER THE AMOUNT DUE:"))
        query="INSERT INTO MAINTENANCE_FEE VALUES({},'{}','{}',{},{})".format(rec_id,flat_no,month,amt_paid,amt_due)
        cur.execute(query)
        mycon.commit()
        ch=input("\nDO YOU WANT TO ADD MORE?(Y/N):")


def UpdatePaymentInfo():
    rec_id=int(input("\nENTER THE RECEIPT ID:"))
    query="SELECT * FROM MAINTENANCE_FEE WHERE RECEIPT_ID={}".format(rec_id)
    cur.execute(query)
    data=cur.fetchone()
    if data==None:
        print("RECORD NOT FOUND")
    else:
        print("\nMENU")
        print("___________")
        print("\nENTER 1 FOR UPDATING THE AMOUNT PAID")
        print("ENTER 2 FOR UPDATING THE DUE AMOUNT")
        ch=int(input("\nENTER YOUR CHOICE:"))
        if ch==1:
            paid=int(input("\nENTER THE PAID AMOUNT:"))
            query="UPDATE MAINTENANCE_FEE SET AMOUNT_PAID={} WHERE RECEIPT_ID={}".format(paid,rec_id)
            cur.execute(query)
            mycon.commit()
            print("\nAMOUNT PAID UPDATED")
        elif ch==2:
            due=int(input("\nENTER THE DUE AMOUNT:"))
            query="UPDATE MAINTENANCE_FEE SET AMOUNT_DUE={} WHERE RECEIPT_ID={}".format(due,rec_id)
            cur.execute(query)
            mycon.commit()
            print("\nAMOUNT DUE UPDATED")
        else:
            print("\nINVALID INPUT")

def displaymaintenacefee():
    cur.execute("SELECT * FROM MAINTENANCE_FEE")
    records=cur.fetchall()
    print("\nMAINTENANCE FEE DETAILS")
    print("________________________________")
    print("\nRECEIPT_ID\t\tFLAT_NUMBER\t\t\tMONTH\t\t\tAMOUNT PAID\t\t\tAMOUNT DUE")
    for row in records:
        print("\n",row[0],"\t\t\t",row[1].ljust(10),"\t\t\t\t",row[2].ljust(10),"\t\t",row[3],"\t\t\t\t",row[4])


def mainmaintenance():
   while True:
      print("\n1.TO ADD MAINTENANCE DETAILS")
      print("2.TO UPDATE MAINTENANCE DETAILS")
      print("3.TO DISPLAY MAINTENANCE DETAILS")
      print("4.EXIT")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         AddMaintenance()
      elif ch==2:
         UpdatePaymentInfo()
      elif ch==3:
         displaymaintenacefee()
      elif ch==4:
         mycon.close()
         break
      else:
         print("INVALID CHOICE")










    
    
    

