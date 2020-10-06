from main.models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_role','profile_pic','phone')


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ('broad', 'narrow','experience','address','state','country')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'username')
        exclude = ()



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['broad','doctor',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.none()

        if 'broad' in self.data:
            try:
                broad_id = int(self.data.get('broad'))
                self.fields['doctor'].queryset = Doctor.objects.filter(broad_id=broad_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.broad.doctor_set.order_by('name')


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('date','time',)
        exclude = ()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','category','body',)
        exclude = ()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name','complaint','investigation','examination',)
        exclude = ()