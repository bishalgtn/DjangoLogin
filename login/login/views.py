from django.shortcuts import render

def home(request):
#    return HttpResponse("Hi, this is home page of the app")
    return render(request, 'home.html')
