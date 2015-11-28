from django.contrib.auth.forms import UserChangeForm

from authentication.models import EmailUser


class EmailUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(EmailUserChangeForm, self).__init__(*args, **kargs)
        #del self.fields['username']


    class Meta:
        model = EmailUser
        fields = ['email', 'password']