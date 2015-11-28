from django.conf.urls import url
from authentication.views.create_user import CreateUserView
from authentication.views.authenticate_user import LoginUserView

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(r'^login/', LoginUserView.as_view(), name='login'),
]
