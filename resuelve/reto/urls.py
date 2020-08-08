from django.urls import path

from . import views

urlpatterns = [
    path('calculate_salaries', views.calculate_salaries),
    path('calculate_salaries_bonus', views.calculate_salaries_bonus),
]
