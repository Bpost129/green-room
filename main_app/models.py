from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Plant(models.Model):
  name = models.CharField(max_length=25)
  plant_type = models.CharField(max_length=25)
  height = models.IntegerField()
  age = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("plant-detail", kwargs={"plant_id": self.id})
  