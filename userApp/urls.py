from django.urls import path
from django.contrib.auth import views as auth_views
from .views import new_usuario

urlpatterns = [
    path('login/', auth_views.LoginView.as_views(
        template_name='user/Login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='user/logout.html'
    ), name='logout'),
    path('new_usuario', new_usuario, name='new_usuario')
]
