from django.db import models

class Feedbacks(models.Model):
	name = models.CharField(max_length=100)
	fakeortrue = models.CharField(max_length=200)
	link = models.CharField(max_length = 500)
	text = models.TextField(max_length=600)

chocies_type = [
	('covid-19','โควิด-19'),
	('hemp','กัญชา'), 
	('bank','ธนาคาร'),
]

class New(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=500)	
	tag = models.CharField(max_length=50 ,choices=chocies_type, default='covid-19')
	image = models.ImageField(upload_to='images', blank=True, null = True)











