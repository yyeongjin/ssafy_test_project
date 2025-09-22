from django.urls import path
from .views import index, num, create, delete

app_name = 'demo_app'
urlpatterns = [
    path('', index, name="index"),
    path('<int:num>/', num, name="num"),
    path('create/', create, name="create"),
    path('<int:num>/delete/', delete, name="delete"),
]
