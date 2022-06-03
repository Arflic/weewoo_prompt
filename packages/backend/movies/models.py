from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  year = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
  rating = models.IntegerField(
    default=1,
    validators=[
      MaxValueValidator(10),
      MinValueValidator(1),
  ])

  class Meta:
    ordering = ['-id']
