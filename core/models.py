from django.db import models
from django.contrib.auth.models import User

DEPT = (('ops','Operative'),('mkt','Marketing'))

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	employee_no = models.IntegerField(unique=True)
	department = models.CharField(DEPT, max_length=15)

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	client_no = models.IntegerField(unique=True)
