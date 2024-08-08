from django.urls import path
from .views import login_user, logout_user, register_user, test_view

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('test/', test_view, name='test'),
]
