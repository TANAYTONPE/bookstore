from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('book_list')
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
        request.session['cart'] = cart
    return redirect('book_list')

@login_required
def view_cart(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'store/cart.html', {'books': books})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('book_list')  # Or wherever you want to go
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'store/login.html')
Book.objects.all()

Book.objects.all()

book = Book.objects.get(id=1)
book.title = "The God of Small Things"
book.author= "Arundhati Roy"
book.price = 100.00
book.save()
book = Book.objects.get(id=2)
book.title = "The Palace of Illusions"
book.author= "Chitra Banerjee Divakaruni"
book.price = 276.00
book.save()
book = Book.objects.get(id=3)
book.title = "Midnight's Children"
book.author= "Salman Rushdie"
book.price = 800.00
book.save()
