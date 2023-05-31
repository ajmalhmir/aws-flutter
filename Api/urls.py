from django.urls import path
from Api import views

urlpatterns = [
    path('Books/',views.BooksList.as_view()),
]