import datetime
from django.db import models

from authentication.models import User


class Post(models.Model):
    user = models.ForeignKey(User, null=False)
    text = models.TextField(null=False, default="")
    created = models.DateTimeField(default=datetime.datetime.now())
