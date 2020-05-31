from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('', views.ImageListView.as_view(), name='list'),
    path('about/', views.about, name='home-about'),
    path('detail/<int:pk>', views.ImageDetailView.as_view(), name='detail'),
    path('upload/', views.ImageUploadByUser.as_view(), name='upload'),
    path('update/<int:pk>', views.ImageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ImageDeleteView.as_view(), name='delete'),

]
