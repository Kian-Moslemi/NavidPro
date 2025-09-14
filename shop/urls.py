from django.urls import path
from . import views

urlpatterns = [
    path('CallUs/',views.call_us,name='callus'),
    path('AboutUs/',views.about_us,name='aboutus'),
    path('SignIn/',views.sign_in,name='signin'),
    path('LogIn/',views.log_in,name='login'),
    path('LogOut/',views.log_out,name='logout'),
    path('HotSandwich/',views.hotsandwich,name='hotsandwich'),
    path('ColdSandwich/',views.coldsandwich,name='coldsandwich'),
    path('Drinks/',views.drinks,name='drinks'),
    path('',views.home_page,name='home')
]
