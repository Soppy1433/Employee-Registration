from django.urls import path, include
from .views import index, delete_employee, update_employee, update

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:empid>", delete_employee, name="delete"),
    path("update_employee/<int:empid>", update_employee, name="update_employee"),
    path("update/<int:empid>", update, name="update"),
]
