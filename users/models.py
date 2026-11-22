from django.db import models
from django.contrib.auth.models import User

class MyCustomUser(User):
    pass
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']

