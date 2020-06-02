from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from home.forms import ImageForm
from django.http import Http404
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
    template_name = 'home/image_list.html'
    context_object_name = 'images'

    def get_queryset(self):

        queryset = {'user_posts': Image.objects.all().filter(author=self.request.user), 'all_posts': Image.objects.all()}
        return queryset


@login_required()
def profile(request):
    user_images = Image.objects.all().filter(author=request.user)
    return render(request, 'users/profile_view.html',  {"all_images": user_images})


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







