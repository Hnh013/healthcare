from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


#############################################################################################################

class Profile(models.Model):
    ROLES =(('Patient','Patient'),('Doctor','Doctor'),('Senior Doctor','Senior Doctor'),('Health Expert','Health Expert'))
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_pic = models.ImageField(default='def.jpg',upload_to="images",null=True, blank=True)
    user_role = models.CharField(max_length=30,choices=ROLES,default="Patient")
    phone = PhoneField(blank=True, help_text='Contact Phone Number')

    def __str__(self):
        return self.user.username

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    balance = models.IntegerField(default=100)
    def __str__(self):
        return self.user.username

class Broad(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Narrow(models.Model):
	broad = models.ForeignKey(Broad, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default="Not Available", blank=True, null=True)

	def __str__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name




class DoctorProfile(models.Model):
	SS = (('Pending','Pending'),('Approved','Approved'))
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE) 
	broad = models.ForeignKey(Broad, on_delete=models.CASCADE) 
	narrow = models.ForeignKey(Narrow, on_delete=models.CASCADE)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	experience = models.IntegerField()
	address = models.TextField()
	approval1 = models.CharField(max_length=50, choices=SS, default="Pending")
	approval2 = models.CharField(max_length=50, choices=SS, default="Pending")

	def __str__(self):
		return self.profile.user.username



#########################################################################################################


class Schedule(models.Model):
    STATUSES = (('Free','Free'),('Booked','Booked'))
    docprof = models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=30,choices=STATUSES,default='Free')


class Booked(models.Model):
    timing = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    pname = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=100,blank=True,null=True)
    

class Patient(models.Model):
	docprof = models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	complaint = models.CharField(max_length=100)
	investigation = models.CharField(max_length=100)
	examination =  models.CharField(max_length=100)

	def __str__(self):
		return self.name

###########################################################################################################



class Doctor(models.Model):

    broad = models.ForeignKey(Broad, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    appt_id = models.CharField(max_length=50,default="C100000")
    broad = models.ForeignKey(Broad, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.doctor.name



class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name




class Post(models.Model):
	author = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	image = models.ImageField(default='21.jpg',upload_to="images",null=True, blank=True)
	body = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	post_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateField(auto_now_add=True)

class Top(models.Model):
	featured = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="featured")
	post1 = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post1")
	post2 = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post2")
	post3 = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post3")
	post4 = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post4")

class Feedback(models.Model):
	email = models.CharField(max_length=100,blank=True,null=True)
	username = models.CharField(max_length=100,blank=True,null=True)
	emoji = models.CharField(max_length=100,blank=True,null=True)
	reply =models.CharField(max_length=500,blank=True,null=True)

class Contact(models.Model):
	email = models.CharField(max_length=100,blank=True,null=True)
	name = models.CharField(max_length=100,blank=True,null=True)
	phone = models.CharField(max_length=100,blank=True,null=True)
	query = models.CharField(max_length=500,blank=True,null=True)
	message = models.CharField(max_length=100,blank=True,null=True) 




