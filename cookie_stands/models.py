from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models


class CookieStand(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    tags = models.JSONField(default=list, null=True)

    def __str__(self):
        return self.name
