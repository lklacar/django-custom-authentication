from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.email_user_creation_form import EmailUserCreateForm
from authentication.models import EmailUser


class CreateUserView(TemplateView):
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        data = {}
        data['form'] = EmailUserCreateForm()
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

    def post(self, request):
        form = EmailUserCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data
            user = EmailUser()
            user.email = data['email']
            user.set_password(data['password1'])
            user.save()


            return HttpResponse("DONE")



        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))
