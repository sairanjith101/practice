CREATE DATABASE students;

USE students;

CREATE TABLE student_info (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  roll_no INT NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_no VARCHAR(15) NOT NULL,
  PRIMARY KEY (id)
);

select * from student_info;