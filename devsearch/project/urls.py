from django.urls import path
from .import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.main, name='main'),
    path('loginUser/', views.loginUser, name = 'loginUser'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('registerUser/', views.registerUser , name = 'registerUser'),
    path('api/category/', views.CategoryAPI.as_view(), name='api_category'),
    path('api_schema/', get_schema_view(title='API schema'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(template_name = 'docs.html', extra_context = {'schema_url':'api_schema'}), name='swagger-ui')
]