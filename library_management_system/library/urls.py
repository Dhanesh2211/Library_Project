"""library_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.index,name='index'),
     path('signup',views.signup,name='signup'),
     path('save_data',views.save_data,name='save_data'),
     path('log',views.log,name='log'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('admin_logout',views.admin_logout,name='admin_logout'),
     path('add_book',views.add_book,name='add_book'),
     path('book_edit',views.book_edit,name='book_edit'),
     path('book_update',views.book_update,name='book_update'),
     path('book_delete',views.book_delete,name='book_delete'),
    #  path('dashboard',views.dashboard,name='dashboard'),



     

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
