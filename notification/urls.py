from django.urls import path
from . import views

urlpatterns = [
    path('notification/', views.notification_list, name="notification"),
    path('read-notification/<int:pk>/', views.read_notification, name='read-notification'),
    path('delete-notification/<int:id>/', views.delete_notification, name="delete-notification"),
]
