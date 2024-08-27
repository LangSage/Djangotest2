# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'myapp'  # Убедитесь, что app_name определено

# myapp/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('add/', views.add_product, name='add_product'),  # Добавляем маршрут для добавления продукта
    path('live_search/', views.live_search, name='live_search'),
]
