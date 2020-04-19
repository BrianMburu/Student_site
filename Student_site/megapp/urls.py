from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
from .views import register,user_login

urlpatterns =[
    path('',views.index,name='index'),
    path('megapp/register/', views.register, name='register'),
    path('megapp/user_login/', views.user_login, name="user_login"),  
    path('new_search/',views.new_search,name='new_search'),
    path('special/',views.special,name='special'),
    path('logout/', views.user_logout, name='logout'),
    path('profile',views.profile , name='profile'),
    path('notes/', views.notes, name = 'notes'),
    path('chat/', views.chat, name = 'chat'),
]