from django.http import HttpResponse
from django.shortcuts import render
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	#tak mozno dobawit template
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	print(args,kwargs)
	#Show which user is currently loged in
	print(request.user)
	#eto prosto verniot tekst http
	#return HttpResponse("<h1>Contact Page</h1>")
	return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>SocialPage</h1>")


def galery_view(request, *args, **kwargs):
	return HttpResponse("<h1>Galery Page</h1>")	

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [1, 2, 3,777, 312, 312, "Abc"]
	}

	#return HttpResponse("<h1>About Page</h1>")	
	return render(request, "about.html", my_context)
	