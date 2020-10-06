from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
import json
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
 
class TestViews(TestCase):
	# def test_blog_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('blog'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_blog_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('blog'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/blog.html')



	# def test_register_user_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('registeruser'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_register_user_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('registeruser'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/register.html')


	# def test_partners_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('partners'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_partners_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('partners'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/partners.html')

	# def test_about_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('about'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_about_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('about'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/about.html')



	
	# def test_index_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('index'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_index_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('index'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/index.html')


	# def test_selfassess_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('selfassess'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_selfassess_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('selfassess'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/selfassess.html')

	# def test_feedback_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('feedback'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_feedback_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('feedback'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/feedback.html')

	# def test_contact_view_accessible_by_name(self):
	# 	response = self.client.get(reverse('contact'))
	# 	self.assertEqual(response.status_code, 200)

	# def test_contact_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('contact'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'main/contact.html')

	


	# def test_dashboard_redirect_if_not_logged_in(self):
	# 	response = self.client.get(reverse('dashboard'))
	# 	self.assertRedirects(response, '/?next=/dashboard/')

	# def test_staffdashboard_redirect_if_not_logged_in(self):
	# 	response = self.client.get(reverse('staffdashboard'))
	# 	self.assertRedirects(response, '/?next=/staffdashboard/')

	
	def test_reset_password_view_accessible_by_name(self):
		response = self.client.get(reverse('reset_password'))
		self.assertEqual(response.status_code, 200)

	def test_reset_password_view_uses_correct_template(self):
		response = self.client.get(reverse('reset_password'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/password_reset.html')










# class LoginTest(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
   
#     def test_login(self):
#     	login = self.client.login(username='temporary', password='temporary')
#     	response = self.client.get(reverse('loginuser'))
#     	self.assertEqual(str(response.context['user']), 'temporary')
#     	self.assertEqual(response.status_code, 200)




