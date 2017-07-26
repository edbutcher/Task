from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from appointments.models import Appointment, AppointmentMember
from django.db import IntegrityError
from . import models


class CreateAppointment(LoginRequiredMixin, generic.CreateView):
    """
    Creation Appointments.
    """
    fields = ('name', 'description', 'date', 'time_start', 'time_end')
    model = Appointment


class SingleAppointment(generic.DetailView):
    """
    Detail single Appointment
    """
    model = Appointment


class ListAppointment(generic.ListView):
    """
    List of Appointments.
    """
    model = Appointment


class JoinAppointment(LoginRequiredMixin, generic.RedirectView):
    """
    Join to Appointment.
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse('appointments:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        appointment = get_object_or_404(Appointment, slug=self.kwargs.get('slug'))

        try:
            AppointmentMember.objects.create(user=self.request.user, appointment=appointment)

        except IntegrityError:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'You are now member!')

        return super().get(request, *args, **kwargs)


class LeaveAppointment(LoginRequiredMixin, generic.RedirectView):
    """
    Leave an Appointment.
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse('appointments:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.AppointmentMember.objects.filter(
                user=self.request.user,
                appointment__slug=self.kwargs.get('slug')
            ).get()
        except models.AppointmentMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are in this group!')
        else:
            membership.delete()
            messages.success(self.request, 'Success')
        return super().get(request, *args, **kwargs)
