from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest,HttpResponse
from django.views.generic import CreateView, ListView, DetailView

from . import models
# import CreateView
from .models import Photo


class PicList(ListView):
    model = Photo
    template_name = 'MytestApp/picture_list.html'
    queryset = Photo.objects.all().order_by('-date')


class PicDetail(DetailView):
    model = Photo
    template_name = 'MytestApp/picture_detail.html'


class PicUpload(CreateView):
    model = Photo
    template_name = 'MytestApp/picture_form.html'
    fields = ['title','img']






























