

# In your urls.py
from django.urls import path
from .views import CustomSignUpView


from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
     #path('', views.login_view, name='login'),
    # path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='a_login'),
    path('signup/', CustomSignUpView.as_view(),name='signup'),
     path('home/', views.home, name='home'),
     path('add-criminal/', views.add_criminal, name='add-criminal'),
     path('search/', views.search_criminal, name='search'),
     path('criminal/<int:criminal_id>/', views.criminal_details, name='criminal-details'),
     path('accounts/', include('allauth.urls')),
 ]
