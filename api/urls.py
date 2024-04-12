from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('posts', views.get_posts, name='post-list'),
    path('tags', views.get_tags, name='tag-list'),
    path('posts/<uuid:pk>', views.post_detail, name='post-detail'),
    path('posts/create', views.create_post, name='create'),
    path('posts/update/<uuid:pk>', views.update_post, name='post-update'),
    path('posts/delete/<uuid:pk>', views.delete_post, name='post-delete'),
]
