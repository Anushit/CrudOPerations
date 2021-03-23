from django.db import models

# Create your models here.
class artist(models.Model):
    Name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.FileField(blank=False,null=True,upload_to='img/')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Crud_artist"