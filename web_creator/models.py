from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.parent:
            return f"{self.parent.get_absolute_url()}/{self.slug}"
        return f"/{self.slug}"
