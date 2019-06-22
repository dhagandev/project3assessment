from django.urls import path
from . import views

urlpatterns = [
	path('', views.ItemList.as_view(), name="home"),
	path('add/', views.AddItem.as_view(), name='add_item'),
	path('delete/<int:pk>', views.DeleteItem.as_view(), name='delete_item'),
]