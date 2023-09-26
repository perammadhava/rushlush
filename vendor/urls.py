from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    path('vendor_profile/',views.vendor_profile,name='vendor_profile'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_product/',views.add_product, name='add_product'),
   
]




