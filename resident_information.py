import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()

def amt_paid():
    query="SELECT AMOUNT_PAID FROM MAINTENANCE_FEE WHERE RECEIPT_ID={}".format(rec_id)
    cur.execute(query)
    s1=cur.fetchone()
    print("\nAMOUNT PAID")
    print("_______________")
    print("\n",s1[0])
    

def amt_due():
    query="SELECT AMOUNT_DUE FROM MAINTENANCE_FEE WHERE RECEIPT_ID={}".format(rec_id)
    cur.execute(query)
    s2=cur.fetchone()
    print("\nAMOUNT DUE")
    print("_______________")
    print("\n",s2[0])
    
    
    
def payment_info():
    cur.execute("SELECT AMOUNT_DUE FROM MAINTENANCE_FEE WHERE RECEIPT_ID={}".format(rec_id))
    s3=cur.fetchone()
    print("\nPAYMENT INFORMATION")
    print("______________________")
    if s3[0]==0:
        print("\nPAYMENT COMPLETED!!")
    else:
        print("\nPAYMENT NOT COMPLETED")


def mainpayment():
    global rec_id
    rec_id=int(input("\nENTER THE RECEIPT ID:"))
    query="SELECT * FROM MAINTENANCE_FEE WHERE RECEIPT_ID={}".format(rec_id)
    cur.execute(query)
    data=cur.fetchone()
    if data==None:
        print("RECORD NOT FOUND")
    else:
       while True:
          print("\n1.TO VIEW TOTAL AMOUNT PAID")
          print("2.TO VIEW TOTAL AMOUNT DUE")
          print("3.TO VIEW PAYMENT INFORMATION")
          print("4.EXIT")
          ch=int(input("\nENTER YOUR CHOICE:"))
          if ch==1:
                amt_paid()
          elif ch==2:
                amt_due()
          elif ch==3:
                payment_info()
          elif ch==4:
                mycon.close()
                break
          else:
                print("INVALID CHOICE")
                     
              



    






    
          

