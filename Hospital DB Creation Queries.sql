create database silverhill_hospital;
use silverhill_hospital;

/* Creating a table consisitng of all the patients that create an account */
CREATE TABLE patients (
    Login_ID INTEGER(6) PRIMARY KEY,
    pwd VARCHAR(20),
    name VARCHAR(30),
    age INT(3),
    DOB DATE,
    gender VARCHAR(10),
    weight DOUBLE(6 , 3 ),
    height DOUBLE(6 , 3 ),
    Blood_Group CHAR(4),
    Emergency_Contact VARCHAR(30) DEFAULT NULL,
    Emergency_Contact_Number BIGINT(10) DEFAULT NULL,
    Patient_Contact_Number BIGINT(10) Unique,
    address VARCHAR(50)
);

/* In double(m,d), m is the TOTAL NUMBER OF DIGITS in the number and d is the numbers after the Decimal point. eg -  for 196.7781 m=6,d=4 */

/*Creating a table containing all doctors along with their basic info and availability */
CREATE TABLE doctors (
    ID INT(6) PRIMARY KEY,
    name VARCHAR(20),
    age INT(3) CHECK (age >= 30),
    dept VARCHAR(20),
    gender VARCHAR(10),
    off_day INT(1)
);
/* off_day tells us during which half of the year the doctor will be working and which will he/she be on leave.*/
/* if off_day is '6' then he/she will be at the hospital for the first 6 month of the year, if it's '12' he/she will be working for the second half of the year */ 

/* Creating some dummy values for the table containing all doctors */
insert into doctors values(000001,"Dr.Manjunath Brar",34,"Pathology","Male",6);
insert into doctors values(000002,"Dr.Naveen Rao",37,"Pathology","Male",12);
insert into doctors values(000003,"Dr.Ankita Sahi",43,"Endocrinology","Female",12);
insert into doctors values(000004,"Dr.Ajay Bafna",33,"Endocrinology","Male",6);
insert into doctors values(000005,"Dr.Sanjay Deepak",56,"Neurology","Male","12");
insert into doctors values(000006,"Dr.Sumukh Katekar",44,"Neurology","Other","6");
insert into doctors values(000007,"Dr.Anjali Thakur",41,"Dermatology","Female","12");
insert into doctors values(000008,"Dr.Diya Kumar",30,"Dermatology","Female","6");
insert into doctors values(000009,"Dr.Karan Shah",36,"Cardiology","Male","6");
insert into doctors values(000010,"Dr.Ananya Purush",37,"Cardiology","Female","12");
insert into doctors values(000011,"Dr.Anushka Shankar",32,"Gynaecology","Female","6");
insert into doctors values(000012,"Dr.Ravi Pandit",56,"Gynaecology","Male","12");
insert into doctors values(000013,"Dr.Hardeep Singh",40,"Orthopaedics","Other","6");
insert into doctors values(000014,"Dr.Harsh Bhandari",43,"Orthopaedics","Male","12");
