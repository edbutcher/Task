from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'avalon_test/test.html'


class ThanksPage(TemplateView):
    template_name = 'avalon_test/thanks.html'


class HomePage(TemplateView):
    template_name = 'avalon_test/index.html'
