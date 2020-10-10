from django.db import models
from items.models import Profile

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

