from django.db import models
from uuid import uuid4
from apps.accounts.models import User
from .base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=500)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent} -->  {self.name}"

