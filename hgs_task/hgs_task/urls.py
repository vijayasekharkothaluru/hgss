from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('', views.Hgs_View.as_view(), name = 'hgs'),
]
