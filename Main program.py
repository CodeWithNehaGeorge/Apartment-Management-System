from programs import flat_management,maintenance_fee,reporting,resident_information,resident_management
import mysql.connector as m
import sys
mycon=m.connect(host="localhost",user="root",passwd="0099",database="APARTMENTMANAGEMENT")
cur=mycon.cursor()

def main():
   print("\nWELCOME TO APARTMENT MANAGEMENT SYSTEM")
   print("__________________________________________________________")
   while True:
      print("\nENTER 1 IF YOU ARE ADMINISTRATOR")
      print("ENTER 2 IF YOU ARE USER")
      print("ENTER 3 TO EXIT")
      ch=int(input("\nENTER YOUR CHOICE:"))
      if ch==1:
         admin=input("\nENTER THE ADMIN ID:")
         password=input("\nENTER THE PASSWORD:")
         if admin=="admin123" and password=="apartment001":
            print("\nLOGIN SUCCESSFUL")
            print("\nWELCOME")
            print("_____________")
            print("\nENTER 1 FOR FLAT MANAGEMENT")
            print("ENTER 2 FOR RESIDENT MANAGEMENT")
            print("ENTER 3 FOR MAINTENANCE COLLECTION")
            print("ENTER 4 FOR STATEMENTS")
            ch=int(input("\nENTER YOUR CHOICE:"))
            if ch==1:
               flat_management.mainflat()
            elif ch==2:
               resident_management.mainresident()
            elif ch==3:
               maintenance_fee.mainmaintenance()
            elif ch==4:
               reporting.mainreporting()
            else:
               print("INVALID CHOICE")
         else:
            print("\nINVALID USERNAME OR PASSWORD")
      elif ch==2:
         resident_information.mainpayment()
      elif ch==3:
         print("\nTHANK YOU")
         sys.exit()
      else:
         print("INAVLID INPUT")
main()



































         
       
            
            
