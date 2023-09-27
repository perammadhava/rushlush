from django.urls import path
from . import views



urlpatterns =[
    path('',views.website,name='website'),
   # path('login_page/',views.login_page,name='login_page'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('vendor_profile/',views.vendor_profile,name='vendor_profile'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_product/',views.add_product, name='add_product'),
    path('index/', views.index, name='index'),
    path('Customerlogin/', views.Customer_login_view, name='Customerlogin'),
    path('Customerregister/', views.Customer_register_view, name='Customerregister'),
    
   
]




