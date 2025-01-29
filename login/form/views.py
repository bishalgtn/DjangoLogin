from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'form.html')


def addBook(request):
    return render(request,'addBook.html')