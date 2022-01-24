from django.db import models


class LogUserActivity(models.Model):
    description = models.TextField()

