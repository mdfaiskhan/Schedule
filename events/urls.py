from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
   # path('home', views.h, name='home'),
    path('create',views.create, name='form'),
    path('detail/<id>',views.detail_view,name="deatils"),
    path('detail/<id>/register',views.register_event,name="register_event"),
     path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]