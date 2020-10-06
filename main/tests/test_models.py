from django.test import TestCase
from django.urls import reverse
from main.models import *
import json
from django.contrib.auth.models import User


# class ModelsTest(TestCase):
#     @classmethod

#     #################################### SETTING UP TEST DATA ############################################

#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         user = User.objects.create(username="Anvil", first_name="Jim", last_name="Neidhart", email="jimanvil@gmail.com", password="Oxygen@8")
        
#         profile = Profile.objects.create(user=user, user_role="Patient", phone="+917251859011")
        
#         bd01 = Broad.objects.create(name="BD01")
        
#         nd01 = Narrow.objects.create(broad=bd01, name="ND01")

#         country = Country.objects.create(name="Canada")

#         state = State.objects.create(country=country,name="Calgary") 

#         docprof = DoctorProfile.objects.create(profile=profile,broad=bd01,narrow=nd01,country=country,state=state,experience=10,address="The Hart Dungeon")

#         schedule = Schedule.objects.create(docprof=docprof,date='2020-10-12',time='10:30:30',status="Free")

#         booked = Booked.objects.create(timing=schedule,pname="DH Smith",payment_id="Pddeafasfasfs")
    

#     ########################################################################################################


#     ################################# TESTING USER MODEL ###################################################  
    
#     def test_username(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('username').verbose_name
#         self.assertEquals(field_label, 'username')

#     def test_first_name(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('first_name').verbose_name
#         self.assertEquals(field_label, 'first name')

#     def test_last_name(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('last_name').verbose_name
#         self.assertEquals(field_label, 'last name')

#     def test_email(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('email').verbose_name
#         self.assertEquals(field_label, 'email address')
        
#     def test_password(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('password').verbose_name
#         self.assertEquals(field_label, 'password')

#     ##########################################################################################################

#     #################################### TESTING PROFILE MODEL ###############################################

#     def test_user_role(self):
#         user = User.objects.get(id=1)
#         profile = Profile.objects.get(user=user)
#         field_label = profile._meta.get_field('user_role').verbose_name
#         self.assertEquals(field_label, 'user role')

#     def test_phone(self):
#         user = User.objects.get(id=1)
#         profile = Profile.objects.get(user=user)
#         field_label = profile._meta.get_field('phone').verbose_name
#         self.assertEquals(field_label, 'phone')

#     ###########################################################################################################

#     #################################### TESTING BROAD DISEASE MODEL ###############################################

#     def test_broad_name(self):
#         bd = Broad.objects.get(id=1)
        
#         field_label = bd._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')
    
#     ###############################################################################################################

#     #################################### TESTING NARROW DISEASE MODEL ###############################################

#     def test_narrow_name(self):
#         bd = Broad.objects.get(id=1)
#         nd = Narrow.objects.get(broad=bd)
#         field_label = nd._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')

#     ###########################################################################################################
    
#     #################################### TESTING COUNTRY MODEL ###############################################

#     def test_country_name(self):
#         country = Country.objects.get(id=1)
        
#         field_label = country._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')
    
#     ###############################################################################################################

#     #################################### TESTING STATE MODEL ###############################################

#     def test_state_name(self):
#         cou = Country.objects.get(id=1)
#         sta = State.objects.get(country=cou)
#         field_label = sta._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')

#     ###########################################################################################################
    
#     #################################### TESTING DOCTORPROFILE MODEL ###############################################

#     def test_docprof_experience(self):
#         pro = Profile.objects.get(id=1)
#         sta = State.objects.get(id=1)
#         cou = Country.objects.get(id=1)
#         bd = Broad.objects.get(id=1)
#         nd = Narrow.objects.get(id=1)

#         docprof = DoctorProfile.objects.get(profile=pro,state=sta,country=cou,broad=bd,narrow=nd)
    
#         field_label = docprof._meta.get_field('experience').verbose_name
#         self.assertEquals(field_label, 'experience')

#     def test_docprof_address(self):
#         pro = Profile.objects.get(id=1)
#         sta = State.objects.get(id=1)
#         cou = Country.objects.get(id=1)
#         bd = Broad.objects.get(id=1)
#         nd = Narrow.objects.get(id=1)

#         docprof = DoctorProfile.objects.get(profile=pro,state=sta,country=cou,broad=bd,narrow=nd)
    
#         field_label = docprof._meta.get_field('address').verbose_name
#         self.assertEquals(field_label, 'address')

#     ###########################################################################################################
    
    
#     #################################### TESTING SCHEDULE MODEL ###############################################

#     def test_schedule_date(self):
#         pro = DoctorProfile.objects.get(id=1)
#         sch = Schedule.objects.get(docprof=pro)
    
#         field_label = sch._meta.get_field('date').verbose_name
#         self.assertEquals(field_label, 'date')

#     def test_schedule_time(self):
#         pro = DoctorProfile.objects.get(id=1)
#         sch = Schedule.objects.get(docprof=pro)
    
#         field_label = sch._meta.get_field('time').verbose_name
#         self.assertEquals(field_label, 'time')

#     def test_schedule_status(self):
#         pro = DoctorProfile.objects.get(id=1)
#         sch = Schedule.objects.get(docprof=pro)
    
#         field_label = sch._meta.get_field('status').verbose_name
#         self.assertEquals(field_label, 'status')
    

#     ###########################################################################################################
    
#     #################################### TESTING BOOKED MODEL ###############################################

    

#     ###########################################################################################################
    





