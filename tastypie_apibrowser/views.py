# Imports from django
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView


@staff_member_required
def staff_member_template(request, *args, **kwargs):
    return TemplateView.as_view(*args, **kwargs)

