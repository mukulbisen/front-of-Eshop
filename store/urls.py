from django.urls import path
from store.views import index, signup

urlpatterns = [
    path('', index),
    path('signup', signup)
]
