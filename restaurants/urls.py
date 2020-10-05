from django.urls import path, re_path
from restaurants import views

urlpatterns = [
    re_path(r'^restaurants/?$', views.RestaurantList.as_view()),
    path('restaurants/<uuid:pk>', views.RestaurantDetail.as_view()),
    path('restaurants/statistics', views.Statistics.as_view()),
]
