"""QuarantineTarantino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from share_experience_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post_detail/<int:experience_id>',views.post_detail,name='post_detail'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('myexperience',views.myexperience,name='myexperience'),
    path('add_experience',views.add_experience,name='add_experience'),
    path('delete_experience/<int:experience_id>',views.delete_experience,name='delete_experience'),
    path('signout',views.signout,name='signout'),
    path('admin/', admin.site.urls),
]
