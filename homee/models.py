from django.db import models

# Create your models here.

class detail(models.Model):
	FOOD_TYPE = (
		('CST/17/SWE/00041','CST/17/SWE/00041'),
		('CST/17/SWE/00021','CST/17/SWE/00021'),
		('CST/17/SWE/00055','CST/17/SWE/00055'),
		('CST/17/SWE/00056','CST/17/SWE/00056'),
		('CST/17/SWE/00043','CST/17/SWE/00043'),
        ('CST/17/SWE/00049','CST/17/SWE/00049'),
		
	)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	PhoneNumber = models.CharField(max_length=11)
	Reg_No = models.CharField(max_length=30, choices = FOOD_TYPE)
	StreetAddress = models.CharField(max_length=50)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)