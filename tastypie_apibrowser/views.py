# Imports from django
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


def StaffMemberView(TemplateView):
    template_name = 'apibrowser/index.html'

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs)
        return super(StaffMemberView, self).dispatch(*args, **kwargs)

