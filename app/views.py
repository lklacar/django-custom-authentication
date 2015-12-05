from django.shortcuts import render, render_to_response
# Create your views here.
from django.template import RequestContext


def index(request):
    return render_to_response("app/index.html", context_instance=RequestContext(request))



def list(request):
    return render_to_response("app/post-list.html", context_instance=RequestContext(request))