from django.db import models

# Project
class Project(models.Model):
    name            = models.CharField(max_length=32)
    title           = models.CharField(max_length=64)
    description     = models.TextField()
    icon_url        = models.CharField(max_length=200)


