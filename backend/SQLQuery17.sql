CREATE TABLE user_reg (
username varchar(255),
firstname varchar (255),
lastname varchar (255),
typeofuser varchar (255),
address1 varchar (255),
phone1 int,
dateofbirthday int,
dateofbirthmonth int,
dateofbirthyear int,
cityofbirth varchar (255),
countryofbirth varchar (255),
sex varchar (255),
maritialstatus varchar (255),
Primary key (username)
);

CREATE TABLE Scholarship_Donation (
amount int,
academic_year int,
scholarshipID int,
username varchar (255),
FOREIGN KEY (scholarshipID) REFERENCES Scholarship (scholarshipID),
FOREIGN KEY (username) REFERENCES user_reg (username)
);

CREATE TABLE School (
schoolID int,
school_name varchar (255),
address1 varchar (255),
city varchar (255),
country varchar (255),
school_type varchar (255),
contact_name varchar(255),
contact_phone varchar (255),
Primary Key (schoolID),
);

CREATE TABLE Student_Scholarship (
awarded_on varchar (255),
delivery_method varchar (255),
award_justification varchar (255),
awarded_amount int,
username varchar (255),
scholarshipID int,
Foreign Key (username) REFERENCES user_reg (username),
Foreign Key (scholarshipID) REFERENCES Scholarship (scholarshipID)
);

CREATE TABLE Scholarship (
scholarshipID int,
denomination varchar (255),
referred_studies varchar (255),
minimum_amount int,
description_sch varchar (255),
criteria varchar (255),
Primary Key (scholarshipID)
);

CREATE TABLE Tuition_Fees (
schoolID int,
academic_level varchar (255),
academic_year varchar (255),
tuition int,
clothing varchar (255),
books int,
misc varchar (255),
FOREIGN KEY (schoolID) REFERENCES School (schoolID),
);

CREATE TABLE Student_Education(
schoolID int,
username varchar(255),
year_attended int,
class varchar(255),
grade varchar(255),
degree varchar(255),
class_rank varchar(255),
dismissed varchar(255),
dismissal_reason varchar(255),
FOREIGN KEY (schoolID) REFERENCES School (schoolID),
FOREIGN KEY (username) REFERENCES user_reg (username),
);

CREATE TABLE Student_Hollow_Year
username varchar(255),
hollow_year int,
activities varchar(255),
FOREIGN KEY (username) REFERENCES user_reg (username),
);

