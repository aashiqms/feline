from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from home.forms import ImageForm
from home.models import Image
from users.models import Profile


def about(request):
    return render(request, 'home/about.html', {'title': 'about'})


class ImageUploadByUser(CreateView, LoginRequiredMixin):

    form_class = ImageForm
    model = Image

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ImageDetailView(DetailView, LoginRequiredMixin):
    model = Image
    queryset = Image.objects.all()


class ImageListView(ListView, LoginRequiredMixin):
    model = Image

    def get_queryset(self):
        return Image.objects.all()


def getting_username(request):
    username = request.user.username
    return render(request, 'home/image_detail.html', {'username': username})


class ImageDeleteView(DeleteView):
    models = Image
    success_url = reverse_lazy('list')

    def get_queryset(self):
        queryset = Image.objects.all().filter(author=self.request.user)
        return queryset



class ImageUpdateView(UpdateView, LoginRequiredMixin):
    model = Image
    form_class = ImageForm

