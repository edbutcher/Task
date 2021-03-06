from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView


class SignUp(CreateView):
    """
    Creation User
    """
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
