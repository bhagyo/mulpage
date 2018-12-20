"""amarproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from blog_post.views import home
from student.views import page1
from blog_post.views import post_list, single_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('page1/', page1, name='page1'),
    path('post-list/', post_list, name='post-list'),
    path('single-post/<post_id>', single_post, name='single-post'),
]
