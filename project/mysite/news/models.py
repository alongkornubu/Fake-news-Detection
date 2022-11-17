from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=100)
	fakeortrue = models.CharField(max_length=200)
	link = models.CharField(max_length = 200)
	detail = models.TextField(blank=True , null= True)

class AddNew(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=500)	
	tag = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images', blank=True, null = True) 


