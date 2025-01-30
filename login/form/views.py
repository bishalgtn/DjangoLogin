from django.shortcuts import render, redirect, HttpResponse
from django.utils.text import slugify
from .models import Student, Book

# Create your views here.
def form(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        if len(phone_number) !=10 or phone_number[0]==0:
            return HttpResponse("Number should be exact 10 and should not start from Zero")
        book = request.POST.get("book")
        slug = request.POST.get("slug")
        if not slug:
            slug = slugify (f"{first_name}-{last_name}")

        student = Student(first_name=first_name, last_name=last_name, email=email,phone_number=phone_number,book=book)
        student.save()

        return redirect('addBook')
    return render(request, 'form.html') 


def addBook(request):
    # books = Book.objects.all()
    if request.method == "POST":
        ISBN = request.POST.get("ISBN")
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        catagory= request.POST.get("catagoty")
        
        book = Book(ISBN=ISBN, title=title, discription = discription, catagory=catagory)
        book.save()
        return HttpResponse("data added")
    return render(request,'addBook.html')
