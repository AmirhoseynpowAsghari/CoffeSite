from django import forms

from django.contrib.auth import get_user_model


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=15, label="First Name", required=True,
                                        help_text='please enter english alphabetics only for First name',
                                        error_messages={
                                            'required': 'reqired first name'},
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'First Name here ..',
                                            'class': 'form-control'})
                                        )

    last_name = forms.CharField(max_length=15, label="Last Name", required=True,
                                help_text='please enter english alphabetics only for Last Name',
                                error_messages={
                                    'required': 'reqired last name'},
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name here ..',
                                    'class': 'form-control'})
                                )


    email = forms.EmailField(max_length=255, label="Email", required=True,
                                 error_messages={'required': 'required email'},
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Email here ..',
                                     'class': 'form-control'})
                                )

    password1 = forms.CharField(label='password', min_length=8, required=True,help_text='use 8 and more', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password configration', min_length=8,required=True, help_text='use 8 and more', widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )








class UserLoginForm(forms.ModelForm):
    class Meta:
        model   = get_user_model()
        fields  = ("email", "password")
        widgets = {
            "password": forms.PasswordInput(),
        }