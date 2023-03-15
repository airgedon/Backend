from django.urls import path
from .import views

urlpatterns = [
    path('', views.main, name='main'),
    path('loginUser/', views.loginUser, name = 'loginUser'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('registerUser/', views.registerUser , name = 'registerUser'),
    path('api/category/', views.CategoryAPI.as_view()),
    path('createCategory', views.createCategory, name='createCategory')
    
]