from django.urls import path
from smartphones import views

urlpatterns = [
    path("", views.smartphone_index, name='manufacturer'),
    path("register-smartphone/", views.register_smartphone, name="register-smartphone")
]