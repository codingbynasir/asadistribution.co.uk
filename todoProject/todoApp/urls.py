from django.urls import path
from . import views

app_name="todoApp"
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('add', views.Create.as_view(), name="add"),
    path('update/<int:pk>', views.Update.as_view(), name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('marked/<int:pk>', views.completed, name="marked"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout, name="logout"),
]
