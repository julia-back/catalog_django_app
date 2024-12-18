from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    preview_img = models.ImageField(upload_to="blog/preview_img/")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    count_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['title']
        db_table = "posts_table"
