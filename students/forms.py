from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class StudentSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_student'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_student')
        model = get_user_model()

        labels = {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email ID',
            'password2': 'Confirm Password',
            'is_student': 'Confirm your details please!',
            }


        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user
