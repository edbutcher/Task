from django.contrib import admin
from appointments.models import Appointment, AppointmentMember

admin.site.register(Appointment)
admin.site.register(AppointmentMember)
