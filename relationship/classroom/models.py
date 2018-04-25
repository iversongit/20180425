from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=10)
    class Meta:
        db_table = "classroom"