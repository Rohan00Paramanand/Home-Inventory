from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_items/', views.add_items, name='add_items'),
    path('find_items/', views.find_items, name='find_items'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_item/<int:pk>', views.delete_item, name='delete_item'),
    path('edit_item/<int:pk>', views.edit_item, name='edit_item'),
]