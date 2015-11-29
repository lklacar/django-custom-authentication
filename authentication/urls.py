from django.conf.urls import url, include
from rest_framework import routers

from authentication.views.api_v1.user_api import AuthenticatedUserViewSet
from authentication.views.create_user_view import CreateUserView
from authentication.views.authenticate_user_view import LoginUserView

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(r'^login/', LoginUserView.as_view(), name='login'),
    url(r'^logout/', "authentication.views.logout.logout", name="logout")
]
