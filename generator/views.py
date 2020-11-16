from django.shortcuts import render
from django.http import HttpResponse as hr
import random
import string
# Create your views here.
def about(request):
    return render(request,'generator/about.html')
def home(request):
    return render(request,'generator/home.html',{'password':"america"})
def password(request):
    thepassword=''
    alpha=list(string.ascii_lowercase)
    length=int(request.GET.get('length'))
    if request.GET.get("upper"):
        alpha.extend(list(string.ascii_uppercase))
    if request.GET.get('Numbers'):
        alpha.extend(list("0123456789"))
    if request.GET.get('special'):
        alpha.extend(list("!@#$%^&*()_+"))
    for i in range(length):
        thepassword+=random.choice(alpha)

    return render(request,'generator/password.html',{'password':thepassword})