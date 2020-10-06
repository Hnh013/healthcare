from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)

admin.site.register(Broad)
admin.site.register(Narrow)

admin.site.register(Country)
admin.site.register(State)

admin.site.register(DoctorProfile)

admin.site.register(Patient)
admin.site.register(Wallet)

admin.site.register(Schedule)
admin.site.register(Booked)

admin.site.register(Appointment)
admin.site.register(Doctor)

admin.site.register(Category)
admin.site.register(Post)

admin.site.register(Comment)
admin.site.register(Top)

admin.site.register(Contact)
admin.site.register(Feedback)


admin.site.site_header = "Medicine India Corporation (MED!CO)"