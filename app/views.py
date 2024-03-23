from django.shortcuts import render
from django import forms
from django.views.generic import FormView
from app.models import Video
from django.core.files.storage import FileSystemStorage

# Create your views here.


class UploadVideoForm(forms.Form):
    file = forms.FileField()
