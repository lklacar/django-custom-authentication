from django.contrib import admin

# Register your models here.
from authentication.models import User
from authentication.models.user_admin import UserAdmin

admin.site.register(User, UserAdmin)