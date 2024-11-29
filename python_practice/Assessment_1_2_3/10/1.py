import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost',
    user = 'root',
    password = '1234',
    database = 'education'
)

mycursor = mydb.cursor()

def add_student(regis_num,name,email,mob_no):
    sql = "INSERT INTO student (regis_num,name,email,mob_no) VALUES (%s,%s,%s,%s)"
    val = (regis_num,name,email,mob_no)
    mycursor.execute(sql,val)
    mysql.commit()
    print(mycursor.rowcount, "record inserted")

regis_num = input("Enter register number : ")
name = input("Enter name : ")
email= input("Enter email id : ")
mob_no = input("Enter mobile number : ")

add_student(regis_num,name,email,mob_no)