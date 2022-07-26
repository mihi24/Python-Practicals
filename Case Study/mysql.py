import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='1234',
         host='localhost',
         database='mysql'
        )

mycursor = conn.cursor()
mycursor.execute("Show databases")

print("The databases in MySql are:")
for i in mycursor:
    print(i)

mycursor.execute("Select * from studentinf")

result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

a = int(input("Enter Prn no."))
b = input("Enter first name")
c = input("Enter middle name")
d = input("Enter last name")
e = input("Enter Address")
f = input("Enter Moblie number")
g = input("Enter Email Id")
h = input("Enter Date of birth")

s = 'INSERT INTO studentinf VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
t = (a,b,c,d,e,f,g,h)
mycursor.execute(s,t)
conn.commit()

mycursor.execute("Select * from studentinf")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

prnNo= int(input("Enter the prn number you want to delete"))
rm = "DELETE from studentinf WHERE prnNo=%s"
val1 = (prnNo,)
mycursor.execute(rm,val1)
conn.commit()

mycursor.execute("Select * from studentinf")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

p = input("Enter existing address")
q = input("Enter new address")
ch = "UPDATE studentinf SET address=%s WHERE address=%s"
val3 = (q,p)
mycursor.execute(ch,val3)
conn.commit()

mycursor.execute("Select * from studentinf")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

col = "ALTER TABLE studentinf ADD CGPA VARCHAR(100) AFTER dob"
prnNo = input("Enter your Prn number")
CGPA = input("Enter CGPA")
cgpaUp = "UPDATE studentinf SET CGPA=%s where prnNo=%s"
val4 = (CGPA,)
mycursor(cgpaUp,val4)
mycursor.execute(col)

mycursor.execute("Select * from studentinf")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

conn.close()