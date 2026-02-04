from django.db import models
from django.core.validators import MinLengthValidator

class Item(models.Model):
    text = models.TextField(
        default='',
        validators=[MinLengthValidator(1)]
    )
