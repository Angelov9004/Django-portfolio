# models.py
from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    facebook = models.URLField()
    Linkedin = models.URLField()
    Github = models.URLField()
    Website = models.URLField()
    Designed_by = models.CharField(max_length=100)
    Designer = models.URLField()

class about(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    birthday = models.DateField()
    age = models.IntegerField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    Freelance = models.BooleanField()
    freetext = models.TextField()

class counts(models.Model):
    clients = models.IntegerField()
    projects = models.IntegerField()
    hours_of_support = models.IntegerField()
    awards = models.IntegerField()

class skills(models.Model):
    skill1 = models.CharField(max_length=100)
    skill1value = models.IntegerField()
    skill2 = models.CharField(max_length=100)
    skill2value = models.IntegerField()
    skill3 = models.CharField(max_length=100)
    skill3value = models.IntegerField()
    skill4 = models.CharField(max_length=100)
    skill4value = models.IntegerField()
    skill5 = models.CharField(max_length=100)
    skill5value = models.IntegerField()
    skill6 = models.CharField(max_length=100)
    skill6value = models.IntegerField()


class interests(models.Model):
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    interest4 = models.CharField(max_length=100)
    interest5 = models.CharField(max_length=100)
    interest6 = models.CharField(max_length=100)
    interest7 = models.CharField(max_length=100)
    interest8 = models.CharField(max_length=100)
    interest9 = models.CharField(max_length=100)
    interest10 = models.CharField(max_length=100)
    interest11 = models.CharField(max_length=100)
    interest12 = models.CharField(max_length=100)


class resume(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()





class expirience(models.Model):
    title = models.CharField(max_length=100)
    years_working = models.IntegerField()
    address_of_company = models.CharField(max_length=100)
    section_1 = models.CharField(max_length=100)
    section_2 = models.CharField(max_length=100)
    section_3 = models.CharField(max_length=100)
    section_4 = models.CharField(max_length=100)

    ##Exprience 2 line
    title2 = models.CharField(max_length=100)
    years_working2 = models.IntegerField()
    address_of_company2 = models.CharField(max_length=100)
    section_12 = models.CharField(max_length=100)
    section_22 = models.CharField(max_length=100)
    section_32 = models.CharField(max_length=100)
    section_42 = models.CharField(max_length=100)


class education(models.Model):
    school_name = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    address_school = models.CharField(max_length=100)
    about_school = models.CharField(max_length=100)

class university(models.Model):
    university_name = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    address_university = models.CharField(max_length=100)
    about_university = models.CharField(max_length=100)

class contact(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()

class services(models.Model):
    service_1 = models.CharField(max_length=100)
    service_1_description = models.TextField()
    service_2 = models.CharField(max_length=100)
    service_2_description = models.TextField()
    service_3 = models.CharField(max_length=100)
    service_3_description = models.TextField()
    service_4 = models.CharField(max_length=100)
    service_4_description = models.TextField()
    service_5 = models.CharField(max_length=100)
    service_5_description = models.TextField()
    service_6 = models.CharField(max_length=100)
    service_6_description = models.TextField()

class portfolio(models.Model):
   project_1 = models.CharField(max_length=100)
   project_1_description = models.TextField()
   project_2 = models.CharField(max_length=100)
   project_2_description = models.TextField()
   project_3 = models.CharField(max_length=100)
   project_3_description = models.TextField()
   project_1_url = models.URLField()
   project_2_url = models.URLField()
   project_3_url = models.URLField()
