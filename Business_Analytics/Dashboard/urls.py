from django.urls import path
from .import views

urlpatterns = [
    path("",views.dashboard),
    path("update/<int:id>/",views.update_value)
]