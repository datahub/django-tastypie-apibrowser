# Imports from django
from django.conf.urls import url, patterns
# from django.views.generic import TemplateView


# Imports from this app
from views import StaffMemberView


urlpatterns = patterns('',
        # (r'^$', staff_member_template, {'template_name':'apibrowser/index.html'},
        #     'name=api-browser'),
        url(r'^$', StaffMemberView.as_view()),
        # url(r'^templates$', TemplateView.as_view(template_name='apibrowser/templates.html')),
    )
