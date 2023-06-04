from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateTimeInput

from .models import Organization, Event


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title', 'description', 'address', 'postcode']
        labels = {
            'title': 'Название организации',
            'description': 'Описание организации',
            'address': 'Адрес',
            'postcode': 'Почтовый индекс'
        }





# class EventForm(forms.ModelForm):
#     organizations = forms.ModelChoiceField(
#         queryset=Organization.objects.all(),
#         widget=forms.CheckboxSelectMultiple(),
#         label='Организации'
#     )

#     date = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'datepicker'}),
#         label='Дата'
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['organizations'].queryset = Organization.objects.all()
#         self.fields['organizations'].label_from_instance = lambda obj: obj.title

#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'organizations', 'image', 'date']
#         labels = {
#             'title': 'Название мероприятия',
#             'description': 'Описание мероприятия',
#             'image': 'Изображение',
#             'date': 'Дата'
#         }






class EventForm(forms.ModelForm):
    organizations = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label='Организации'
    )

    date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Дата и время'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organizations'].queryset = Organization.objects.all()
        self.fields['organizations'].label_from_instance = lambda obj: obj.title

    class Meta:
        model = Event
        fields = ['title', 'description', 'organizations', 'image', 'date']
        labels = {
            'title': 'Название мероприятия',
            'description': 'Описание мероприятия',
            'image': 'Изображение',
            'date': 'Дата'
        }

# class EventForm(forms.ModelForm):
#     organizations = forms.ModelMultipleChoiceField(
#         queryset=Organization.objects.all(),
#         widget=forms.Select(),
#         label='Организации'
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['organizations'].queryset = Organization.objects.all()
#         self.fields['organizations'].label_from_instance = lambda obj: obj.title

#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'organizations', 'image', 'date']
#         labels = {
#             'title': 'Название мероприятия',
#             'description': 'Описание мероприятия',
#             'image': 'Изображение',
#             'date': 'Дата'
#         }
        


