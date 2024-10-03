from django.urls import path, include
from . import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name = 'todo_home'),
    path('del/<str:item_id>', views.delete_note, name = "delete_note"),
]