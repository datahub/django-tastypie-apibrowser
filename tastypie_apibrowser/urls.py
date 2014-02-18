# Imports from django
from django.conf.urls import url, patterns
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView


urlpatterns = patterns('',
        url(r'^$', staff_member_required(TemplateView.as_view(template_name='apibrowser/index.html'))),
        url(r'^templates$', TemplateView.as_view(template_name='apibrowser/templates.html')),
    )
