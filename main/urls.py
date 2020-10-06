from django.urls import include, path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),

    path('selfassess/', views.selfassess, name='selfassess'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('staffdashboard/', views.staffdashboard, name='staffdashboard'),
   path('admindashboard/', views.admindashboard, name='admindashboard'),

  path('loginuser/', views.loginuser, name='loginuser'),
  path('registeruser/', views.registeruser, name='registeruser'),
  path('logoutuser/', views.logoutuser, name='logoutuser'),
  path('change_password/', views.change_password, name='change_password'),

  path('partners/',views.partners, name="partners"),
  path('patientdetail/<str:id>', views.patientdetail, name='patientdetail'),
  path('createpatient/', views.createpatient, name='createpatient'),
  path('editpatient/<str:id>', views.editpatient, name='editpatient'),

  path('deletepatient/<str:id>', views.deletepatient, name='deletepatient'),
  path('blog/',views.blog,name='blog'),
  path('createblog/',views.createblog,name='createblog'),
  path('updateblog/<str:id>',views.updateblog,name='updateblog'),
  path('deleteblog/<str:id>',views.deleteblog,name='deleteblog'),

  path('blogdetail/<str:id>',views.blogdetail,name='blogdetail'),
  path('like_post/<int:id>', views.like_post, name='like_post'),
  path('comment_post/', views.comment_post, name='comment_post'),
  path('forms/',views.forms,name='forms'),
  path('walletpay/<str:id>',views.walletpay,name='walletpay'),
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name='password_reset_complete'),
    path('cancel/<str:id>',views.cancel, name="cancel"),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
     path('complete_doctorprofile/', views.complete_doctorprofile, name='complete_doctorprofile'),
    path('update_doctorprofile/', views.update_doctorprofile, name='update_doctorprofile'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic'),
   path('update_phone/', views.update_phone, name='update_phone'),
   path('approval/',views.approval,name='approval'),
   path('seniorapproval/<str:id>',views.seniorapproval,name='seniorapproval'),

   path('expertapproval/<str:id>',views.expertapproval,name='expertapproval'),
  path('adddoctor/<str:id>',views.adddoctor,name='adddoctor'),
    path('choose/',views.choose,name='choose'),
     path('load_doctors/', views.load_doctors, name='load_doctors'),

   path('booking/',views.booking,name='booking'),
    path('bookmeet/<str:id>',views.bookmeet,name='bookmeet'),
     path('preview/',views.preview,name='preview'),
     path('app_charge/',views.app_charge,name='app_charge'),

    path('createschedule/',views.createschedule,name='createschedule'),
     path('reschedule/<str:id>',views.reschedule,name='reschedule'),
      path('deleteschedule/<str:id>',views.deleteschedule,name='deleteschedule'),
      path('createwallet/',views.createwallet,name='createwallet'),
      path('recharge/',views.recharge,name='recharge'),
      path('rechargewallet/',views.rechargewallet,name='rechargewallet'),

    
]

