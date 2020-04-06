INSERT INTO Scholarship (scholarshipID, denomination, referred_studies, minimum_amount, description_sch, criteria)
VALUES('123','Catholic','Computers','2000','Scholastic','GPA');

INSERT INTO Student_Scholarship (awarded_on, delivery_method, award_justification, awarded_amount, username, scholarshipID)
VALUES('4199','deposit','scholastic','2000','ASU','123');

INSERT INTO School (schoolID, school_name, address1, city, country, school_type, contact_name, contact_phone)
VALUES('3244','Corona','456_E_Ninth_ST','Chandler','United_States','HighSchool','Miss_Right','6023459860');

INSERT INTO Scholarship_Donation (amount, academic_year, scholarshipID, username)
VALUES('3500','2020','123','ASU');

INSERT INTO Student_Education (schoolID, username, year_attended, class, grade, degree, class_rank, dismissed, dismissal_reason)
VALUES('3244','ASU','2020','2020','Senior','Associates','12th',null,null);

INSERT INTO Student_Hollow_Year (username, hollow_year, activities)
VALUES('ASU','2020','Sports');

INSERT INTO Tuition_Fees (schoolID, academic_level, academic_year, tuition, clothing, books, misc)
VALUES('3244','Senior','2020','20000','500','250','200');
