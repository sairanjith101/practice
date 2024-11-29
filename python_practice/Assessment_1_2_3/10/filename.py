import mysql.connector


# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Tamilnadu@246",
  database="students"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Insert student information into the database
def add_student(name, roll_no, email, phone_no):
    sql = "INSERT INTO student_info (name, roll_no, email, phone_no) VALUES (%s, %s, %s, %s)"
    val = (name, roll_no, email, phone_no)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Prompt the user to enter student information
name = input("Enter name: ")
roll_no = input("Enter roll no: ")
email = input("Enter email: ")
phone_no = input("Enter phone no: ")

# Insert the student information into the database
add_student(name, roll_no, email, phone_no)