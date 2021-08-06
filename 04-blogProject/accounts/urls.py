from django.urls import path
from .views import SignUpView
urlpatterns=[
    path('sign/',SignUpView.as_view(), name='signup'),
]