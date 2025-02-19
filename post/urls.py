from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>', views.PostDelete.as_view()),
    path('weather/<str:slug>/', views.weather_page),
]