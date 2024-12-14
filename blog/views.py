from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = BlogPost


class BlogDetailView(DetailView):
    model = BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
