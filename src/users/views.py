# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, FormView

from chat.models import Message
from users.forms import MyUserForm, UserProfileForm
from users.models import MyUser, UserProfile

import django.contrib.auth.urls


def login_user(request):
    template = 'pages/sign-in.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('search-post')

    return render(request, template)


def logout_user(request):
    logout(request)
    return redirect('index')


class IndexListView(ListView):
    model = MyUser
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['muser_pk'] = MyUser.objects.get(email=self.email)
        return context


class MyUserCreateView(CreateView):
    model = MyUser
    form_class = MyUserForm
    template_name = 'pages/sign-up.html'
    success_url = reverse_lazy('index-user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['submit_text'] = 'Sign up'
        return context


# MyUser list view
class MyUserListView(ListView):
    model = MyUser


class MyUserDetailView(DetailView):
    model = MyUser

    def get_object(self, **kwargs):
        return get_object_or_404(MyUser, email=self.kwargs.get('user'))


class MyUserUpdateView(UpdateView):
    model = MyUser
    form_class = MyUserForm
    success_url = reverse_lazy('index-user')

    def get_object(self, **kwargs):
        return get_object_or_404(MyUser, email=self.kwargs.get('user'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['submit_text'] = 'Update'
        return context


class MyUserDeleteView(DeleteView):
    model = MyUser
    success_url = reverse_lazy('index-user')

    def get_object(self, **kwargs):
        return get_object_or_404(MyUser, email=self.kwargs.get('user'))


# UserProfile ListView
class UserProfileListView(ListView):
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_list'] = MyUser.objects.all()
        return context


# Userprofile DetailView
class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        return get_object_or_404(UserProfile, id=self.kwargs.get('id'))


# UserProfile CreateView
class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Sign up'
        return context

    def get_success_url(self):
        return reverse('detail-user-profile', kwargs={'id': self.object.pk})


# UserProfile UpdateView
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update'
        return context

    def get_object(self, **kwargs):
        return get_object_or_404(UserProfile, id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('detail-user-profile', kwargs={'id': self.object.pk})


# UserProfile DeleteView
class UserProfileDeleteView(DeleteView):
    model = UserProfile
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        return get_object_or_404(UserProfile, id=self.kwargs.get('id'))

    success_url = reverse_lazy('index')
