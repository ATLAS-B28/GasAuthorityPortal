from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register_page/', views.register_page, name='register_page'),
    path('submit_req/', views.submit_req, name='submit_req'),
    path('service_track_requests', views.service_track_requets, name='service_track_requests'),
    path('modify_req/<int:req_id>', views.modify_req, name='modify_req'),
    path('delete_req/<int:req_id>', views.delete_req, name='delete_req')
]
