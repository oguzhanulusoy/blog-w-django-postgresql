from django.db import models

class Post(models.Model):

    identifier = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(max_length=180, null=False, blank=False)
    article = models.TextField(max_length=5000, null=False, blank=False)
    date = models.DateField(auto_now=True)
    viewers = models.PositiveIntegerField()
    category = models.CharField(max_length=50, blank=True)
    upload = models.ImageField(upload_to='uploads/', null=True, blank=True)

