from django.db import models
from core.models import *

UNIT = (('mls','Milliliters'),('pls','Pellets'))
class Products(models.Model):
	code = models.CharField(primary_key=True, max_length = 2)
	product = models.CharField(max_length = 15)
	units = models.CharField(choices = UNIT , max_length = 11)
	price = models.IntegerField()
	quantity = models.IntegerField()
	unit_price = models.IntegerField()

	def __str__(self):
		return '{0} | {1} , worth {4} per {2} {3}'.format(self.code, self.product, self.quantity, self.units, self.unit_price)


class ReceivedProducts(models.Model):
	reception_no = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	product = models.ForeignKey(Products, on_delete = models.PROTECT, null=False, blank= False)
	quantity = models.IntegerField()

	def __str__(self):
		return 'Reception {6}: On {5}, {2} {3} of {0} | {1} worth {4} was received.'.format(self.product.code, self.product, self.quantity, self.product.units, self.product.totals, self.date, self.reception_no)

class IssuedProducts(models.Model):
	issuance_no = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	issued_to = models.ForeignKey(Employee, on_delete = models.PROTECT, null=False, blank= False)
	product = models.ForeignKey(Products, on_delete = models.PROTECT, null=False, blank= False)
	client = models.ForeignKey(Client, on_delete = models.PROTECT, null=False, blank= False)
	jen_no = models.IntegerField()
	quantity = models.IntegerField()

	def __str__(self):
		return 'Issuance {6}: On {5}, {2} {3} of {0} | {1} worth {4} was issued to {7} under JEN {8} for {9}.'.format(self.product.code, self.product, self.quantity, self.product.units, self.product.totals, self.date, self.issuance_no, self.issued_to, self.jen_no, self.client)

class ReturnedProducts(models.Model):
	return_no = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	returned_by = models.ForeignKey(Employee, on_delete = models.PROTECT, null=False, blank= False)
	product = models.ForeignKey(Products, on_delete = models.PROTECT, null=False, blank= False)
	client = models.ForeignKey(Client, on_delete = models.PROTECT, null=False, blank= False)
	jen_no = models.IntegerField()
	quantity = models.IntegerField()
	def __str__(self):
		return 'Return {6}: On {5}, {2} {3} of {0} | {1} worth {4} was returned by {7} under JEN {8} for {9}.'.format(self.product.code, self.product, self.quantity, self.product.units, sel.product.totals, self.date, self.return_no, self.returned_by, self.jen_no, self.client)
