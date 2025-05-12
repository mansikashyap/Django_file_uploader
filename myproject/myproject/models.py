from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_data = 'auth_user'

class File(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    s3_key = models.CharField(max_length=500)  # Stores S3 object key
    size = models.BigIntegerField()
    mime_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.filename        