# from django.urls import path
# from . import views

# urlpatterns = [
#     # path(渡す形式, 渡すモジュール先, モジュール先の関数名)
#     path('', views.post_list, name='post_list'),
#     # <int:pk> == int型の変数pkをviewに渡す
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]