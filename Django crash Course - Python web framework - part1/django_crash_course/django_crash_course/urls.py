from django.contrib import admin
from django.urls import path
from django_crach_course_app import views  # Adjust to your actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', views.home),
]
