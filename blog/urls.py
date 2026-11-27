from blog import views
from django.urls import include, path

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('blogs/', views.post_list_view, name='blog_list'), #READ ALL
    path('create/', views.create_post_view, name='create_blog'), #CREATE
    path('blogs/<int:blog_id>/', views.post_detail_view, name='blog_detail'), #READ
    path('blogs/<int:blog_id>/update/', views.post_update_view, name='blog_update'), #UPDATE
    path('blogs/<int:blog_id>/delete/', views.post_delete_view, name='blog_delete'), #DELETE

    path('generate_blog/', views.ai_generate_blog_view, name='generate_blog'), #GENERATE BLOG WITH AI 
]
