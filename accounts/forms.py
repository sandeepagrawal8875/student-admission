from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['full_name','email','phone','password1']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
