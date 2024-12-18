from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        object_ = super().get_object(queryset)
        object_.count_views += 1
        object_.save()
        return object_


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
