from django.http import HttpResponse
from django.shortcuts import render
import datetime


def say_hello(request):
	name = "Bootcamp"
	html = "<html><body><h1>Hello %s!</h1></body></html>" % name
	return HttpResponse(html)


def get_now(request):
	now = datetime.datetime.now()
	return render(request, "HelloWorld_app/templates/HelloWorld/base.html", {"current_date:now"})
