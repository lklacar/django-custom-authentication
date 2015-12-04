from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from authentication.forms.create_user import CreateUserForm
from authentication.models import User


class CreateUserView(TemplateView):
    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        data = {'form': CreateUserForm()}

        if request.user.is_authenticated():
            return redirect("/")

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

    def post(self, request):
        form = CreateUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data
            user = User()
            user.email = data['email']
            user.set_password(data['password1'])
            user.save()

            return redirect("/")

        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))
