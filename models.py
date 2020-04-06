from django.db import models

class user_reg(models.Model):
username = model.PrimaryKey(maxlength=30)
firstname = models.CharField(maxlength=30)
lastname = models.CharField(maxlength=30)
typeofuser = models.CharField(maxlength=30)
address = models.CharField(maxlength=50)
dob_day = models.CharField(maxlength=30)
dob_month = models.CharField(maxlength=30)
dob_year = models.CharField(maxlength=30)
city_of_birth= models.CharField(maxlength=60)
country_of_birth = models.CharField(maxlength=50)
sex = models.CharField(maxlength=30)
marital_status = models.CharField(maxlength=30)

def _str_(self):
    return self.name
  
class Scholarship(models.Model):
scholarshipID = models.PrimaryKey(maxlength=30)
denomination = models.CharField(maxlength=30)
referred_studies = model.CharField(maxlength=30)
minimum_amount = models.Int(maxlength=30)
description_sch = models.CharField(maxlength=30)
criteria = models.CharField(maxlength=30)

def _str_(self):
    return self.name
   
class Scholarship_Donation(models.Model):
amount = models.Int(maxlength=30)
academic_year = models.CharField(maxlength=30)
scholarshipID = model.ForeignKey(Scholarship, maxlength=30)
username = models.ForeignKey(user_reg, maxlength=30)

def _str_(self):
    return self.name
  
class School(models.Model):
schoolID = model.PrimaryKey(maxlength=30)
schoolname = models.CharField(maxlength=30)
address1 = models.CharField(maxlength=50)
city= models.CharField(maxlength=60)
country = models.CharField(maxlength=50)
school_type = models.CharField(maxlength=30)
contact_name = models.CharField(maxlength=30)
contact_phone = models.CharField(maxlength=30)

def _str_(self):
    return self.name

class Student_Education(models.Model):
schoolID = model.ForeignKey(School, maxlength=30)
username = models.ForeignKey(user_reg, maxlength=30)
year_attended = models.CharField(maxlength=50)
class= models.CharField(maxlength=60)
grade = models.CharField(maxlength=50)
degree = models.CharField(maxlength=30)
class_rank = models.CharField(maxlength=30)
dismissed = models.CharField(maxlength=30)
dismissal_reason = models.CharField(maxlength=30)

def _str_(self):
    return self.name
 
class Student_Hallow_Year(models.Model):
username = models.ForeignKey(user_reg, maxlength=30)
hollow_year = models.CharField(maxlength=30)
activities = model.CharField(Scholarship, maxlength=30)

def _str_(self):
    return self.name
  
class Student_Scholarship(models.Model):
awarded_on = model.CharField(maxlength=30)
delivery_method = models.CharField(maxlength=30)
award_justification = models.CharField(maxlength=50)
awarded_amount = models.CharField(maxlength=60)
username = models.ForeignKey(user_reg, maxlength=30)
scholarshipID = models.ForeignKey(Scholarship, maxlength=30)

def _str_(self):
    return self.name
  
class Tuition_Fees(models.Model):
schoolID = model.ForeignKey(School, maxlength=30)
academic_level = model.CharField(maxlength=30)
academic_year= models.CharField(maxlength=30)
tuition = models.CharField(maxlength=50)
clothing = models.CharField(maxlength=60)
books = models.CharField(maxlength=30)
misc = models.CharField(maxlength=30)

def _str_(self):
    return self.name
  
