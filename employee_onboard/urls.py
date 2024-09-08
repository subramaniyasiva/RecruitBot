from django.contrib import admin
from django.urls import path
from recruitbot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.details_view, name='details_view'),  # Use a valid name here
    path('details-updated/', views.details_updated_view, name='details_updated'),
]
