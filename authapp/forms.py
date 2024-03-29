from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import ShopUser
from django import forms


class ShopUserLoginForm(AuthenticationForm):
    """
    форма логина юзера на модели ShopUser
    """
    class Meta:
        model = ShopUser
        # fields = ('username', 'password', 'age')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(self, *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    """
    Форма регистрации юзера на модели ShopUser
    """
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.help_text = ''

    # Проверка возраста
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class ShopUserEditForm(UserChangeForm):
    """
    Форма редактирования юзера на модели ShopUser
    """
    username = forms.CharField(label='Логин')

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    # Проверка возраста
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

