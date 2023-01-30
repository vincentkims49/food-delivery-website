from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Region(models.Model):
	r_name = models.CharField(max_length=20)
	image = models.ImageField(upload_to='regions',null=True,blank=True)
	r_desc = models.CharField(max_length=50)

	def __str__(self):
		return str(self.r_name)

class Region_manager(models.Model):
	region = models.OneToOneField(Region,on_delete=models.CASCADE)
	r_email = models.EmailField()

	def __str__(self):
		return str(self.region)
	

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	profile_pic = models.ImageField(upload_to = 'profiles',null=True,blank=True)
	c_email = models.EmailField()
	# name = models.CharField(max_length=30)
	c_phone_number = models.CharField(max_length=10)
	c_region = models.ForeignKey('Region', on_delete=models.CASCADE)
	address = models.CharField(max_length=20)
	@property
	def get_name(self):
		return self.user.first_name+" "+self.user.last_name
	@property
	def get_id(self):
  		return self.user.id
	def __str__(self):
		return self.user.first_name

class Food(models.Model):
	f_price = models.PositiveIntegerField()
	f_name = models.CharField(max_length=20)
	image_1 = models.ImageField(upload_to='food',null=True,blank=True)
	image_2 = models.ImageField(upload_to='food',null=True,blank=True)
	image_3 = models.ImageField(upload_to='food',null=True,blank=True)
	f_desc = models.CharField(max_length=50)

	def __str__(self):
		return str(self.f_name)

class Orders(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	date_ordered = models.DateTimeField(auto_now_add=True)
	expected_time = models.DateTimeField()
	food = models.ForeignKey('Food',on_delete=models.CASCADE)
	total_price = models.DecimalField(max_digits=5, decimal_places=2)
	# status = models.BooleanField()
	status=models.CharField(max_length=50,null=True,choices=(
        ('approved','approved'),
        ('Delivery in progress','Delivery in progress'),
	 )
	 )

	def __str__(self):
		return str(self.food)

class Feedback(models.Model):
	user = models.ForeignKey(Customer,on_delete=models.CASCADE, null = True, blank=True)
	date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	feed = models.CharField(max_length=100)

	def __str__(self):
		return self.user


class Offers(models.Model):
	food = models.ForeignKey(Food,on_delete=models.CASCADE)
	region = models.ForeignKey('Region',on_delete=models.CASCADE)
	offer_expiry = models.DateTimeField()
	percentage = models.PositiveIntegerField(default=25)

	def __str__(self):
		return str(self.food) 
	

class monthly_plan(models.Model):
	food = models.ForeignKey('Food',on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	delivery_time = models.DateTimeField()

	# def __str__(self):
	# 	return str(self.customer), "'s",str(self.food),"delivery at ",str(self.delivery_time) 


