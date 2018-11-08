from django.forms import ModelForm
from .models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class ProductsForm(ModelForm):
	class Meta:
		model = Products

		fields= [
			'code',
			'product',
			'unit',
			'price',
			'quantity',
			'unit_price',]
			

		labels= {
			'code':_('Code'),
			'product':_('Product'),
			'unit':_('Unit'),
			'price':_('Price'),
			'quantity':_('Quantity'),
			'unit_price':_('Unit Price'),}

class ReceivedProductsForm(ModelForm):
	class Meta:
		model = ReceivedProducts

		fields= [
			'reception_no',
			'date',
			'product',
			'quantity',]
			

		labels= {
			'reception_no':_('Reception Number'),
			'date':_('Date')
			'product':_('Product'),
			'quantity':_('Quantity'),}

class IssuedProductsForm(ModelForm):
	class Meta:
		model = IssuedProducts

		fields= [
			'issuance_no',
			'date',
			'issued_to',
			'product',
			'client',
			'jen_no',
			'quantity',]
			

		labels= {
			'issuance_no':_('Issuance Number'),
			'date':_('Date'),
			'issued_to':_('Issued To'),
			'product':_('Product')
			'client':_('Client'),
			'jen_no':_('Jen Number'),
			'quantity':_('Quantity'),
			}


class ReturnedProductsForm(ModelForm):
	class Meta:
		model = ReturnedProducts

		fields= [
			'issuance_no',
			'date',
			'returned_by',
			'product',
			'client',
			'jen_no',
			'quantity',]
			

		labels= {
			'issuance_no':_('Issuance Number'),
			'date':_('Date'),
			'returned_by':_('Returned By'),
			'product':_('Product')
			'client':_('Client'),
			'jen_no':_('Jen Number'),
			'quantity':_('Quantity'),
			}
