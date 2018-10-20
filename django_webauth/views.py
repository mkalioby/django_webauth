from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def logout(request):
    auth.logout(request)
    context = csrf(request)
    return render_to_response("login.html", context)


def home(request):
    return render_to_response("home.html",{},context_instance = RequestContext(request))
def login(request):
    context=csrf(request)
    if request.method=="GET":
        return render_to_response("login.html",context)
    else:
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            context["invalid"]=True
            return render_to_response("login.html", context)