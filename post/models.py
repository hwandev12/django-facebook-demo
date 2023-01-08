from django.db import models
from authentication.models import CustomUser

import uuid

class FacebookPost(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    author = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    post_text = models.TextField(blank=False)
    post_image = models.ImageField(upload_to='posts/', blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Post facebook"