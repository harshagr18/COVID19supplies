from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    #path('calc/', views.calc, name='page-calc'),
]
