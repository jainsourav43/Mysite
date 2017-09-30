from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Extras(models.Model):
	roll_no = models.CharField(max_length =20)
	date  =  models.DateField()
	item = models.CharField(max_length =50)
	quantity = models.IntegerField(default=0)
	extra =models.IntegerField(default=0)

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	roll_no = models.CharField(max_length=10)
	reg_no = models.CharField(max_length=10)
	extra = models.IntegerField(default=0)
	type_id =models.CharField(max_length=20)
	mess = models.CharField(max_length=2,default='A')

class items(models.Model):
	name = models.CharField(max_length=50)
	cost = models.IntegerField(default=0)
	mess = models.CharField(max_length=2,default='A')
