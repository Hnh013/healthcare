from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import *
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.views.decorators.csrf import csrf_exempt
import random

import razorpay

import json

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import random


import razorpay

import json

from django.db.models import F


razorpay_client = razorpay.Client(auth=("rzp_test_qvsBaHe2xMjIVU","3CoHmIbkifoU4rg7RsNO5EOa"))


def walletpay(request, id):
    firstname = request.user.first_name
    lastname = request.user.last_name
    full_name = firstname + ' ' + lastname

    Schedule.objects.filter(id=id).update(status="Booked")

    schedule = Schedule.objects.get(id=id)

    fix = Booked.objects.create(timing=schedule,pname=full_name,payment_id="Wallet Payment")
    fix.save()

    Wallet.objects.filter(balance=request.user.wallet.balance).update(balance=F('balance')- 31)

    return redirect('dashboard')





@csrf_exempt
def app_charge(request):
    if request.method == "GET":
        amount = 5100
        payment_id  = (request.GET['razorpay_payment_id'])

        razorpay_client.payment.capture(payment_id, amount)

        data = razorpay_client.payment.fetch(payment_id)

        schedule_id = data['notes']['shopping_order_id']
        patient_name = data['description']
        payment_id = data['id']

        #print(timing_id)
        #print(patient_name)
        #print(payment_id)

        Schedule.objects.filter(id=schedule_id).update(status="Booked")

        schedule = Schedule.objects.get(id=schedule_id)

        fix = Booked.objects.create(timing=schedule,pname=patient_name,payment_id=payment_id)
        fix.save()

        context = {'data':data}

        return render(request, 'main/preview.html', context)



def forms(request):
	return render(request, 'main/forms.html')

def index(request):
    top = Top.objects.get(id=1)
    context={'top':top}
    return render(request, 'main/index.html', context)

def about(request):
	return render(request, 'main/about.html')




@login_required(login_url='index')
def admindashboard(request):
    
    patients = Patient.objects.count()

    bookings = Booked.objects.count()

    context = {'bookings':bookings, 'patients':patients}

    return render(request, 'main/admindashboard.html', context)








@login_required(login_url='index')
def staffdashboard(request):
    all_patients = Patient.objects.all()
    docprof = request.user.profile.doctorprofile
    blogs = Post.objects.filter(author=docprof)
    patient = Patient.objects.filter(docprof=docprof)
    patients = Patient.objects.filter(docprof=docprof).count()
    booking = Schedule.objects.filter(docprof=docprof)
    bookings = Schedule.objects.filter(docprof=docprof).count()

    context = {'all_patients':all_patients,'booking':booking, 'patient':patient, 'blogs':blogs,'bookings':bookings, 'patients':patients}

    return render(request, 'main/staffdashboard.html', context)


@login_required(login_url='index')
def dashboard(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    full_name = firstname + ' ' + lastname
    booking = Booked.objects.filter(pname=full_name)
    patient = Patient.objects.filter(name=full_name)

    context = {'booking':booking, 'patient':patient}
    return render(request, 'main/dashboard.html', context)

def cancel(request, id):
    booked = Booked.objects.get(id=id)
    timing_id = booked.timing.id

    Schedule.objects.filter(pk=timing_id).update(status="Free")

    booked.delete()

    return redirect('dashboard')


def approval(request):
    profiles = DoctorProfile.objects.all()
    doctors = Doctor.objects.all()

    context = {'profiles':profiles, 'doctors':doctors}

    return render(request, 'main/approval.html', context)

def seniorapproval(request, id):
    DoctorProfile.objects.filter(pk=id).update(approval1='Approved')

    return redirect('approval')

def expertapproval(request, id):
    DoctorProfile.objects.filter(pk=id).update(approval2='Approved')

    return redirect('approval')

def adddoctor(request,id):
    docprof = DoctorProfile.objects.get(pk=id)
    first_name = docprof.profile.user.first_name
    last_name = docprof.profile.user.last_name
    bd = docprof.broad.name

    broad = Broad.objects.get(name=bd) 


    fullname = first_name + ' ' + last_name

    d = Doctor.objects.create(broad=broad, name=fullname)
    d.save()

    return redirect('approval')


def selfassess(request):
	num = random.randint(1,10)
	if request.method == "POST":
		diabetes = request.POST.get('diabetes')
		
		if num % 5 == 1:
			status = "BD01"
			context = {'status':status}
			return render(request, 'main/selfassess.html', context)
		elif num % 5 == 2:
			status = "BD02"
			context = {'status':status}
			return render(request, 'main/selfassess.html', context)
		elif num % 5 == 3:
			status = "BD03"
			context = {'status':status}
			return render(request, 'main/selfassess.html', context)
		elif num % 5 == 4:
			status = "BD04"
			context = {'status':status}
			return render(request, 'main/selfassess.html', context)
		else:
			status = "No disease"
			context = {'status':status}
			return render(request, 'main/selfassess.html', context)

		return HttpResponse("form invalid!")

	return render(request, 'main/selfassess.html')





    
def partners(request):
	return render(request, 'main/partners.html') 


	


def contact(request):
	if request.method == "POST":
		email = request.POST.get('email')
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		query = request.POST.get('query')
		message = request.POST.get('message')

		contact = Contact.objects.create(email=email,name=name,phone=phone,query=query,message=message)
        contact.save()

		return redirect('contact')
	else:
		return render(request, 'main/contact.html')

	return render(request, 'main/contact.html')




def feedback(request):
	if request.method == "POST":
		email = request.POST.get('email')
		username = request.POST.get('username')
		emoji = request.POST.get('emoji')
		reply = request.POST.get('reply')

		feedback = Feedback.objects.create(email=email,username=username,emoji=emoji,reply=reply,message=message)
        feedback.save()
		return redirect('feedback')
	else:
		return render(request, 'main/feedback.html')

	return render(request, 'main/feedback.html')


def createwallet(request):
    user = request.user
    wallet = Wallet.objects.create(user=user,balance=100)
    wallet.save()
    return redirect('dashboard')


def rechargewallet(request):
    return render(request, 'main/rechargewallet.html')

    
@csrf_exempt
def recharge(request):
    if request.method == "GET":
        amount = 10000
        payment_id  = (request.GET['razorpay_payment_id'])

        razorpay_client.payment.capture(payment_id, amount)

        data = razorpay_client.payment.fetch(payment_id)

        schedule_id = data['notes']['shopping_order_id']
        patient_name = data['description']
        payment_id = data['id']

        #print(timing_id)
        #print(patient_name)
        #print(payment_id)

        amount = amount/100 

        Wallet.objects.filter(balance=request.user.wallet.balance).update(balance=F('balance')+ amount)


        context = {'data':data}

        return render(request, 'main/preview.html', context)






########################################################################################################
########################## LOGIN & REGISTRATION VIEWS BEGIN ##############################################

def loginuser(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context= {}
    return render(request, 'main/index.html', context)


def logoutuser(request):
    logout(request)
    return redirect('index')


def registeruser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Welcome to Sproad ,"+ user +" Your account was successfully created!")
            return redirect('index')

        else:
        	for msg in form.error_messages:
        		messages.error(request, f"{msg}: {form.error_messages[msg]}")

    
    context = {'form':form}
    return render(request, 'main/register.html', context)

############################# LOGIN & REGISTRATION VIEWS END ##############################################
###########################################################################################################


############################################################################################################
############################# PROFILE UPDATION VIEWS BEGIN  ##########################################

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html', {'form': form})


def complete_profile(request):
    if request.method == "POST":
        form1 = ProfileForm(request.POST)
        
        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.user = request.user
            
            profile.save()

           
            return redirect(reverse('dashboard'))

    else:
        form1 = ProfileForm()

    return render(request, 'main/complete_profile.html', {'form1':form1})


def complete_doctorprofile(request):
    if request.method == "POST":
        form1 = DoctorProfileForm(request.POST)
        
        if form1.is_valid():
            docprof = form1.save(commit=False)
            docprof.profile = request.user.profile
            
            docprof.save()

           
            return redirect(reverse('dashboard'))

    else:
        form1 = DoctorProfileForm()

    return render(request, 'main/complete_doctorprofile.html', {'form1':form1})


def update_doctorprofile(request):
    if request.method == "POST":
        form1 = DoctorProfileForm(request.POST,instance=request.user.profile.doctorprofile)
        if form1.is_valid():
            form1.save()
            return redirect(reverse('dashboard'))

    else:
        form1 = DoctorProfileForm(instance=request.user.profile.doctorprofile)
        context = { 'form1': form1 }

        return render(request, 'main/update_doctorprofile.html', context)


def update_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))

    else:
        form = EditProfileForm(instance=request.user)
        context = { 'form': form }

        return render(request, 'main/update_profile.html', context)


def update_profile_pic(request):
	  
    prof = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=prof)
        if form.is_valid():
            
            form.save()

            
            
            return redirect(reverse('update_profile_pic'))
            

    else:
        form = ProfileForm(instance=prof)
        context={'form':form}
        return render(request, 'main/update_profile_pic.html', context)


def update_phone(request):
    prof = request.user.profile


    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=prof)
        if form.is_valid():
            
            form.save()

            messages.success(request, "Image Updated !")
            
            return redirect(reverse('dashboard'))
            messages.success(request, "Image Updated !")
        messages.success(request, "Image Updated !")

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'main/update_phone.html', {'form':form})


############################ PROFILE UPDATION VIEWS END #################################################
###########################################################################################################


####################################################################################################################
####################### BOOKING AND SCHEDULE VIEWS BEGIN ###########################################################

def choose(request):
    num = random.randint(1000,999999)
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.appt_id = num
            newpost.save()
            return booking(request,num)
    return render(request, 'main/choose.html', {'form': form})


def load_doctors(request):
    broad_id = request.GET.get('broad_id')
    doctors = Doctor.objects.filter(broad_id=broad_id).all()
    return render(request, 'main/doctor_dropdown_list_options.html', {'doctors': doctors})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def booking(request,num):
    appt_no = str(num)
    appt = Appointment.objects.get(appt_id=num)

    d = appt.doctor.name

    name = d.split()
    first_name = name[0] 
    last_name = name[1]

    user = User.objects.get(first_name=first_name,last_name=last_name)

    prof = Profile.objects.get(user=user)
    docprof = DoctorProfile.objects.get(profile=prof)

    schedule = Schedule.objects.filter(docprof=docprof)

    context = {'appt':appt, 'docprof':docprof, 'schedule':schedule}

    return render(request, 'main/booking.html',context)


def bookmeet(request,id):
    schedule = Schedule.objects.get(id=id)

    context = {'schedule':schedule}

    return render(request,'main/bookmeet.html',context)


def preview(request):
    if request.method == "POST":
        schedule_id = request.POST.get('schedule_id')
        fullname = request.POST.get('fullname')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        context = {'fullname':fullname,'schedule_id':schedule_id,'doctor':doctor,'date':date,'time':time,'phone':phone,'email':email}
        return render(request, 'main/preview.html',context)

    else:
        schedule = Schedule.objects.get(id=schedule_id)
        context = {'schedule':schedule}

        return render(request, 'main/bookmeet.html', context)


def createschedule(request):

    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            s.docprof = request.user.profile.doctorprofile
            s.save()
            return redirect('staffdashboard')

    else:
        form = ScheduleForm()
        

        return render(request, 'main/createschedule.html', {'form':form})


def reschedule(request, id):
    schedule = Schedule.objects.get(pk=id)
    prof = request.user.profile.doctorprofile
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)

        if form.is_valid():
            s = form.save(commit=False)
            s.docprof = prof
            s.save()

            return redirect(reverse('staffdashboard'))

    else:
        form = ScheduleForm(instance=schedule)
        

    return render(request, 'main/createschedule.html', {'form':form})


def deleteschedule(request, id):
    Schedule.objects.filter(pk=id).delete()
    return redirect(reverse('staffdashboard'))


############################## BOOKING AND SCHEDULE VIEWS END ############################################
##########################################################################################################

###########################################################################################################
############################## PATIENT REPORT VIEWS BEGIN #################################################

def createpatient(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        complaint = request.POST.get('complaint')
        examination = request.POST.get('examination')
        investigation = request.POST.get('investigation')
        docprof = request.user.profile.doctorprofile


        patient = Patient.objects.create(docprof=docprof,name=name,complaint=complaint,investigation=investigation,examination=examination)
        patient.save()


        return redirect('staffdashboard')
    else:
        return redirect('staffdashboard')

    return redirect('staffdashboard')

    
def patientdetail(request, id):

    patient = Patient.objects.get(id=id)

    context = {'patient':patient}

    return render(request, 'main/patientdetail.html', context)


def editpatient(request, id):
    p = Patient.objects.get(pk=id)
    prof = request.user.profile.doctorprofile
    if request.method == "POST":
        form = PatientForm(request.POST, instance=p)

        if form.is_valid():
            s = form.save(commit=False)
            s.docprof = prof
            s.save()

            return redirect(reverse('staffdashboard'))

    else:
        form = PatientForm(instance=p)
        

    return render(request, 'main/patient.html', {'form':form})

    
def deletepatient(request,id):
    Patient.objects.filter(pk=id).delete()
    return redirect(reverse('staffdashboard'))
    

############################## PATIENT REPORT VIEWS END ###########################################################
###########################################################################################################


#######################################################################################################
####################################### BLOGGING VIEWS BEGIN #####################################################

def blog(request):
    posts = Post.objects.all()
    top = Top.objects.all()

    context = {'posts':posts, 'top':top}

    return render(request, 'main/blog.html', context)


def blogdetail(request,id):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=post)
    numcom = Comment.objects.filter(post=post).count()
    stuff = get_object_or_404(Post, id=id)

    likes = stuff.total_likes()

    liked=False
    if stuff.likes.filter(id=request.user.id).exists():
        liked=True

    context = {'post':post, 'likes':likes, 'liked':liked, 'comments':comments, 'numcom':numcom}

    return render(request, 'main/blogdetail.html', context)


def createblog(request):
    cate = Category.objects.all()

    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES.get('image')
        title = request.POST.get('title')
        cat = request.POST.get('category')

        category = Category.objects.get(name=cat)
        body = request.POST.get('body')

        docprof = request.user.profile.doctorprofile

        post = Post.objects.create(author=docprof,image=image,title=title,body=body,category=category)

        post.save()
        return redirect('blog')
    else:
        cate = Category.objects.all()
        context = {'cate':cate}
        return render(request, 'main/createblog.html', context)

    cate = Category.objects.all()
    context = {'cate':cate}

    return render(request, 'main/createblog.html', context)


def updateblog(request,id):
    p = Post.objects.get(pk=id)
    prof = request.user.profile.doctorprofile
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=p)

        if form.is_valid():
            s = form.save(commit=False)
            s.author = prof
            s.save()

            return redirect(reverse('blog'))

    else:
        form = PostForm(instance=p)
        

    return render(request, 'main/updateblog.html', {'form':form})


def deleteblog(request,id):
    Post.objects.filter(pk=id).delete()
    return redirect(reverse('staffdashboard'))

    
def like_post(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists() :
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True


    
    return HttpResponseRedirect(reverse('blogdetail', args=[str(id)]))


def comment_post(request):
    user = request.user.username
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        body = request.POST.get('body')

        post = Post.objects.get(id=post_id)

        comment = Comment.objects.create(post=post,name=user, body=body)

        comment.save()

        return HttpResponseRedirect(reverse('blogdetail', args=[str(post_id)]))

    else:
        return HttpResponseRedirect(reverse('blogdetail', args=[str(post_id)]))
   
    return HttpResponseRedirect(reverse('blogdetail', args=[str(post_id)]))


###################################### BLOGGING VIEWS END ###################################################
#########################################################################################################