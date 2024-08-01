from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('communities/', views.community_list, name='community_list'),
    path('community/<int:pk>/', views.community_detail, name='community_detail'),
    path('community/<int:pk>/join/', views.join_community, name='join_community'),
    path('community/<int:pk>/leave/',
         views.leave_community, name='leave_community'),
    path('community/<int:pk>/send_message/',
         views.send_message, name='send_message'),
    path('posts/', views.post_list, name='post_list'),
    path('new/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('idea/<int:idea_id>/', views.idea_detail, name='idea_detail'),
#     path('dashboard/', dashboard, name='dashboard'),
#     path('edit_profile/', edit_profile, name='edit_profile'),
#     path('follow/<int:user_id>/', follow_user, name='follow_user'),
#     path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
#     path('profile/<int:user_id>/', user_profile, name='profile'),
    path('contributors/', views.contrib, name='contrib'),
]
