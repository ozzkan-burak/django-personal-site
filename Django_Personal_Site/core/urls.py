from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Ana sayfa için bir yönlendirme ekleyin
]