import uuid
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    post_title = models.CharField(max_length=255, null=True)
    post_sub_title = models.CharField(max_length=255, null=True)
    post_description = models.TextField(max_length=1000000, null=True)
    live_url = models.CharField(max_length=100000, blank=True, null=True)
    code_url = models.CharField(max_length=100000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    post_tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return str(self.post_title)
    


  