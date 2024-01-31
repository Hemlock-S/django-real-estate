from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        class UserForm(UserCreationForm):
            class Meta:
                model = User
                fields = ["email", "username", "first_name", "last_name"]
                error_class = "error"


class CustomUserChangeForm(UserChangeForm):
      class UserForm(UserCreationForm):
          class Meta:
              model = User
              fields = ["email", "username", "first_name", "last_name"]
              error_class = "error"
