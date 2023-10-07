from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('register/', RegisterUser.as_view())
]