from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import Post, Category
from .utils import DataMixin





class PostHome(LoginRequiredMixin, DataMixin, ListView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'content'

    login_url = reverse_lazy('login')

    # extra_context = {
    #     'title': 'Home',
    # }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('cat')





class PostCategory(LoginRequiredMixin, DataMixin, ListView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'content'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['content'][0].cat))
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')




class ShowPost(LoginRequiredMixin, DataMixin, DetailView):
    model = Post
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'content'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['content'].title)
        context = dict(list(context.items()) + list(c_def.items()))
        return context






class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'news/add_post.html'
    context_object_name = 'content'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add Post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context




class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'news/login/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(DataMixin):
    pass




def logout_user(request):
    logout(request)
    return redirect('login')


# def index(request):
#     context = {
#         'title': 'Home',
#         'content': Post.objects.all()
#     }
#     return render(request, 'news/index.html', context)


# def show_post(request, post_slug):
#     item = get_object_or_404(Post, slug=post_slug)
#     context = {
#         'title': item.title,
#         'content': item
#     }
#     return render(request, 'news/post.html', context)


# def show_category(request, cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     items = Post.objects.filter(cat_id=cat[0].pk)
#
#     if len(items) == 0:
#         raise Http404()
#
#     context = {
#         'title': cat[0].title,
#         'content': items
#     }
#     return render(request, 'news/index.html', context)



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'news/about.html', context)


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 # Post.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Error add post')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'title': 'Add Post',
#         'form': form
#     }
#     return render(request, 'news/add_post.html', context)


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'news/contacts.html', context)



def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

