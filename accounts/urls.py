from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup,logoutview


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logoutview, name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
]
