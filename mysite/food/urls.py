from django.urls import path , include
from food import views


app_name = 'food'

urlpatterns = [

    # Function base index view
    # path('home/' , views.index, name='index'),

    # Class base index view
    path('home/', views.IndexClassView.as_view(), name = 'index'),

    # Function base detail view
    path('detail/<int:item_id>/', views.detail, name='detail'),

    # Function base create item view
    path('add/', views.create_item, name='create_item'),

    # Function base update item view
    path('update/<int:id>/',views.update_item, name='update_item'),

    # Function base delete item view
    path('delete/<int:id>/', views.delete_item,name= 'delete_item'),


]
