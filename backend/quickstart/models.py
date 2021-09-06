from django.db import models

# Create your models here.


class HandImage(models.Model):
    # image = models.CharField(max_length=200)
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=255, default="img.jpg")
    uploaded_at = models.DateTimeField(auto_now_add=True)
