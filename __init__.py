import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="0099")
print("\nYOUR MYSQL CONNECTION HAS BEEN ESTABLISHED")
cur=mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS APARTMENTMANAGEMENT")
cur.execute("USE APARTMENTMANAGEMENT")





   
   



   
   
   

