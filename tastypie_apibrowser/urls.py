# Imports from django
from django.conf.urls import patterns
from django.views.generic import TemplateView


# Imports from this app
# from views import staff_member_template


urlpatterns = patterns('',
    # (r'^$', staff_member_template, {'template_name':'apibrowser/index.html'},
        # 'name=api-browser'),
        (r'^templates$', TemplateView.as_view(
            template_name='apibrowser/templates.html'),
            'name=api-browser-templates'),
    )

