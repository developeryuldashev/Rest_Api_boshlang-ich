from django.urls import path
from .views import (BlogListView,
                    BlogDetalView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView)

urlpatterns=[
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('',BlogListView.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetalView.as_view(), name='post_detail'),
    path('post/<int:pk>/post_edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),

]