from django import forms

from uploads.core.models import Shapefile


class ShapefileForm(forms.ModelForm):
    class Meta:
        model = Shapefile
        fields = ('description', 'shapefile', )
