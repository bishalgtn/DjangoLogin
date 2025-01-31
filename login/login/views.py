from django.shortcuts import render
from form.models import Student, Book

def home(request):
    books = Book.objects.all()
    students = Student.objects.all()
    data = []
    for i in range(len(students)):
        if i < len(books):
            data.append((students[i], books[i]))
        else:
            data.append((students[i], None))
    return render(request, 'home.html', {'data':data})


def showStudent(request):
    student = Student.objects.all()
    return render(request,'studentData.html',{'students':student})

def showBook(request):
    books = Book.objects.all()
    return render(request, 'bookData.html',{'books':books})