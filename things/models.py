from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)  # must be unique, must not be blank, and must consist of 30 characters or less.
    description = models.CharField(max_length=120, blank=True)  # need not be unique, may be blank, and must consist of 120 characters of less.
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])  # need not be unique, and must be an integer value between 0 and 100 (inclusive).