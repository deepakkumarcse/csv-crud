from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),
]
