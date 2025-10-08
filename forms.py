from django import forms
from .models import AnimalReport
from .models import UserProfile
from .models import Event

class AnimalReportForm(forms.ModelForm):
    class Meta:
        model = AnimalReport
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'fname', 'mname', 'lname', 'email', 'contact_no', 'gender', 'city', 'age', 'bday', 'course', 'school', 'numpets', 'tagone', 'tagtwo', 'tagthree', 'caption']


class EventsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
