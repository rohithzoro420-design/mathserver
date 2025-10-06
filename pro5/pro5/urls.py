from django.contrib import admin
from django.urls import path
from app5 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.calculate_power,name="calculate_power"),
]