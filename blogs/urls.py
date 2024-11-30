from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]

# http://127.0.0.1:8000/category/1  (1,2,3,4,5)