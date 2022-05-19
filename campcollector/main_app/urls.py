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
    path('campgrounds/<int:camp_id>/add_agency/', views.add_agency, name='add_agency'),
    path('campgrounds/<int:camp_id>/assoc_features/<int:features_id>/', views.assoc_features, name='assoc_features'),
    path('campgrounds/<int:camp_id>/unassoc_features/<int:features_id>/', views.unassoc_features, name='unassoc_features'),
    path('campgrounds/<int:camp_id>/add_photo', views.add_photo, name='add_photo'),
    path('features/', views.FeaturesList.as_view(), name='features_index'),
    path('features/<int:pk>/', views.FeaturesDetail.as_view(), name='features_detail'),
    path('features/create/', views.FeaturesCreate.as_view(), name='features_create'),
    path('features/<int:pk>/update/', views.FeaturesUpdate.as_view(), name='features_update'),
    path('features/<int:pk>/delete/', views.FeaturesDelete.as_view(), name='features_delete'),
]
