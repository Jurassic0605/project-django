from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('registro/', views.registerPage),
    path('link/', views.post),
    path('link/<int:id>', views.post),
    path('comment/', views.comment),
]