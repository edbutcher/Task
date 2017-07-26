from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library


class Appointment(models.Model):
    """
    Appointment model.
    """
    name = models.CharField(max_length=255, unique=True)
    date = models.CharField(max_length=255, null=False, blank=False)
    time_start = models.CharField(max_length=255, null=False, blank=False)
    time_end = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='AppointmentMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('appointments:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class AppointmentMember(models.Model):
    """
    AppointmentMember model.
    """
    appointment = models.ForeignKey(Appointment, related_name='memberships')
    date = models.CharField(max_length=255, null=False, blank=False)
    time = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, related_name='user_appointment')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('appointment', 'user')
