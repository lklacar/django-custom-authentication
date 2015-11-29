from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


class LoginUserView(TemplateView):
    template_name = "authentication/login.html"

    def get(self, request, *args, **kwargs):
        data = {}
        data['form'] = AuthenticationForm()
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print form.cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            print request.user.is_authenticated()
            if user:
                return HttpResponseRedirect('/')

        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))
