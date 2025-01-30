from django.shortcuts import render
from form.models import Student, Book

def home(request):
#    return HttpResponse("Hi, this is home page of the app")
    books = Book.objects.all()
    student = Student.objects.all()
    return render(request, 'home.html', {'students':student, 'books': books})


# def show_student(request):
#     student = Student.objects.all()
#     return render(request,'home.html',{'student':student})

# def showBook(request):
#     book = Book.objects.all()
#     return render(request, 'home.html',{'book':book})