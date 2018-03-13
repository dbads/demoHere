from django.conf.urls import url
from django.shortcuts import render
from django.conf import settings as django_settings
from django.core.mail import send_mail

def home(request):
	return render(request,'demoHere/home.html',{})

def subscribe(request):
	print('inside contact')
	email = request.POST.get('email')
	message = 'A subscription request on Demo Here'
	subject = 'Demo here email'
	to_user = [django_settings.EMAIL_HOST_USER]
	from_user = django_settings.EMAIL_HOST_USER
	send_mail(subject,message,from_user,to_user,fail_silently=False)

	return HttpResponse('success')

