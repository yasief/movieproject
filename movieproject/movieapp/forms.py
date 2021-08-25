from django import forms
from .models import Movie


class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["name", "year", "duration", "genre", "desc", "starring", "img"]
