from django.urls import path

from store import views


urlpatterns = [
    path('', views.MainListAPIView.as_view()),

    path('<int:parent_id>/posts/',
         views.CategoryPostListAPIView.as_view()),

    path('<int:parent_id>/category/<int:category_id>/posts/',
         views.CategoryPostListAPIView.as_view()),
]

