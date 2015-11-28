from django.contrib import admin

# Register your models here.
from authentication.models import EmailUser
from authentication.models.email_user_admin import EmailUserAdmin

admin.site.register(EmailUser, EmailUserAdmin)