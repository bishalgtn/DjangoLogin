from django.shortcuts import render
from form.models import Student, Book

def home(request):
    books = Book.objects.all()
    student = Student.objects.all()
    return render(request, 'home.html', {'students':student, 'books': books})


def showStudent(request):
    student = Student.objects.all()
    return render(request,'studentData.html',{'students':student})

def showBook(request):
    books = Book.objects.all()
    return render(request, 'bookData.html',{'books':books})