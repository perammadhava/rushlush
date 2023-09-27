from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Product 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ProductForm,CustomerRegistrationForm,CustomerLoginForm

# Create your views here.

def website(request):
    return render(request,'website.html')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

# def login_page(request):
#     return render(request,'login_page.html')
    


from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('vendor_profile')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    
    return render(request, 'login.html')


      

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


def Customer_register_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['confirm_password']
            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not the same!!")
            else:
                form.save()  # Save the form data to the Vendor model
                return redirect('Customerlogin')
    else:
        form = CustomerRegistrationForm()

   

    return render(request, 'Customerregister.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def Customer_login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            Customer = authenticate(request, username=username, password=password)
            
            if Customer is not None:
                # Log in the user
                login(request, Customer)
                return redirect('/')  # Redirect to a valid URL, e.g., 'home'
            else:
                messages.info(request,'invalid credentials')
        else:
            form = CustomerLoginForm()
    else:
        form = CustomerLoginForm()

    return render(request, 'Customerlogin.html', {'form': form})

   
   
   







