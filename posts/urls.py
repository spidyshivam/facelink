from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/like/', views.post_like, name='post_like'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
]

