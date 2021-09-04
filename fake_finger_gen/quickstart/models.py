from django.db import models

# Create your models here.


class HandImage(models.Model):
    # image = models.CharField(max_length=200)
    file = models.FileField(blank=False, null=False)
    # description = models.CharField(max_lenth=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
