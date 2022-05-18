from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('campgrounds/', views.campgrounds_index, name="index"),
    path('campgrounds/<int:camp_id>', views.campground_detail, name="detail"),
    path('campgrounds/create/', views.CampCreate.as_view(), name='campgrounds_create'),
    path('campgrounds/<int:pk>/update/', views.CampUpdate.as_view(), name='campgrounds_update'),
    path('campgrounds/<int:pk>/delete/', views.CampDelete.as_view(), name='campgrounds_delete'),
]
