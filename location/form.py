from django import forms

from location.models import Location, Image


class CreateImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class CreateLocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['title', 'description', 'leisure', 'region', 'difficulty']

