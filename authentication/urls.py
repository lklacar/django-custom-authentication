from django.conf.urls import url
from authentication.views.create_user_view import CreateUserView
from authentication.views.login_user_view import LoginUserView

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(r'^login/', LoginUserView.as_view(), name='login'),
]
