from django.urls import path
from . import views
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path("blog_list/", views.BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog_create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog_update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog_delete/<int:pk>/", views.BlogDeleteView.as_view(), name="blog_delete"),
]
