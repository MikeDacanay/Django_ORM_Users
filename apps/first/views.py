from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *
# Create your views here.
def index(request):
	users_data = {
		"users_database": Users.objects.all()
	}
	# print Users.objects.values().all()
	return render(request,'first/index.html',users_data)

def new(request):
	return render(request,'first/new.html')

def add(request):
	x = request.POST['firstname_form']
	y = request.POST['lastname_form']
	z = request.POST['email_form']
	Users.objects.create(first_name = x, last_name = y, email= z)
	return redirect('/users/')

def show(request, idx):
	user_show={
		"show": Users.objects.get(id=idx)
	}
	return render(request,'first/show.html',user_show)

def edit(request, idx):
	user_edit={
		"edit": Users.objects.get(id=idx)
	}
	return render(request,'first/edit.html', user_edit)

def update(request,idx):
	x = request.POST['firstname_form']
	y = request.POST['lastname_form']
	z = request.POST['email_form']
	user = Users.objects.get(id=idx)
	user.first_name=x
	user.last_name=y
	user.email=z
	user.save()
	return redirect('/users/')