from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
@admin.site.register
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    written_date = models.DateTimeField(default=timezone.now)
    writer = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"