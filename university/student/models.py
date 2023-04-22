from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
