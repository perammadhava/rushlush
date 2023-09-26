from django.shortcuts import render,redirect
from . models import Product 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request,'home.html')
    


def login(request):

    if request.method != 'POST':
        return render(request,'login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('vendor_profile')
    else:
        messages.info(request,'invalid credentials')
        return redirect('login')    

def register(request):

    if request.method != 'POST':
        return render(request,'register.html')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']

    if password1 == password2:
       if User.objects.filter(username=username).exists():
           messages.info(request,'Username Taken')
           return redirect ('register')
       elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect ('register')
       else:       
        user = User.objects.create_user(username=username,password = password1,email=email,first_name=first_name,last_name=last_name)
        user.save();
        print('user created')
        return redirect('login')
    else:
       messages.info(request,'password is not matching')
       return redirect ('register')
    return redirect('vendor_profile')

def logout(request):
    auth.logout(request)
    return redirect ('/')
 

         # Import the ProductForm if not already imported

from django.shortcuts import render, redirect
from .forms import ProductForm
  # Import messages for displaying error messages

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Set the user for the product
            product.save()  # Save the product with the user
            return redirect('/vendor_profile/')  # Redirect to the appropriate page after successful submission
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})



from django.shortcuts import render
from .models import Product  # Import the Product model
from django.contrib.auth.decorators import login_required  # Import the login_required decorator

@login_required
def vendor_profile(request):
    # Retrieve all products associated with the logged-in user
    products = Product.objects.filter(user=request.user)
    
    return render(request, 'vendor_profile.html', {'products': products})







