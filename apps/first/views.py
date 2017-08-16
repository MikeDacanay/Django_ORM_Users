from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request,'first/index.html')

def new(request):
	print "hello"
	return redirect('/users')
