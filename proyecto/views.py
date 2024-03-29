from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import permission_required, login_required
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from datetime import datetime
import time
from django.conf import settings
from io import BytesIO
from django.views.generic import View
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from proyecto.models import Basurero
# Create your views here.

#Donde salen todos los basureros
#def principal(request):
#	return render(request, 'principal.html')
class BasureroList(ListView):
	model=Basurero
	template_name='principal.html'

def Base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'index.html')

def basureros(request):
	return render(request, 'basureros.html')
