from django.urls import path
from .views import HomeView, CustomLoginView, CustomLogoutView, AddItemView, EditItemView, DeleteItemView, FindItemView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_items/', AddItemView.as_view(), name='add_items'),
    path('find_items/', FindItemView.as_view(), name='find_items'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('delete_item/<int:pk>', DeleteItemView.as_view(), name='delete_item'),
    path('edit_item/<int:pk>', EditItemView.as_view(), name='edit_item'),
]