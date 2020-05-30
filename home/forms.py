from django import forms

from home.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_description', 'tag_someone')
