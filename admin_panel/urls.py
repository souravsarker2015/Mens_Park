from django.urls import path
from django.contrib.auth import views as auth_view
from admin_panel.forms import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product-detail/<int:pk>', views.product_details, name="product-detail"),
    path('shirt/', views.shirts, name='shirt'),
    path('shirt_details/<slug:data>', views.shirts, name='shirt_details'),
    path('pant/', views.pants, name='pant'),
    path('pant_details/<slug:data>', views.pants, name='pant_details'),
    path('watch/', views.watches, name='watch'),
    path('watch_details/<slug:data>', views.watches, name='watch_details'),
    path('tie/', views.ties, name='tie'),
    path('tie_details/<slug:data>', views.ties, name='tie_details'),
    path('shoe/', views.shoes, name='shoe'),
    path('shoe_details/<slug:data>', views.shoes, name='shoe_details'),
    path('search_items', views.search_items, name='search'),
    path('registration/', views.registration, name='registration'),
    path('account/login/', auth_view.LoginView.as_view(template_name='admin_panel/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
]
