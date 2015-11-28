from django.contrib.auth.forms import UserCreationForm

from authentication.models import EmailUser


class EmailUserCreateForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(EmailUserCreateForm, self).__init__(*args, **kargs)



    class Meta:
        model = EmailUser
        fields = ("email",)

        error_messages = {
            'email': {
                'required': "You must enter a valid email address.",
                "unique": "There already exists a user with that email address",

            }
        }
