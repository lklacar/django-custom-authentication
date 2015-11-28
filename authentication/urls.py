from django.conf.urls import url

from authentication.views.create_user_view import CreateUserView

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),

]
