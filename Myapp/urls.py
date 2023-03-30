from Myapp import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name="Home"),
    path('Emplist',views.Emplist,name="Emplist"),
    path('Add_items',views.Add_items,name="Add_items"),
    path('Update/<int:pk>',views.Update_items,name='Update-items'),
    path('delete/<int:pk>',views.delete_items,name='delete-items'),
]