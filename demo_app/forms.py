from django.contrib.auth.forms import UserCreationForm

from demo_app.models import Login


class officerform(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','phone','age','qualification','address','photo')

class farmerform(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','phone','age','address','photo')