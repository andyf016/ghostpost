"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ghostapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newpost/', views.post_form_view, name='newpost'),
    path('boasts/', views.boast_view, name='boasts'),
    path('roasts/', views.roast_view, name='roasts'),
    path('sorted/', views.sorted_view, name='sorted'),
    path('upvote/<int:post_id>/', views.upvote_view, name='upvote'),
    path('downvote/<int:post_id>/', views.downvote_view, name='downvote'),
    path('admin/', admin.site.urls),
]
"""
admin/
index/
boasts/
roasts/
add-post/
upvote/ <int:id>
downvote/<int:id>
sorted/ 
posts/<str:id>
"""