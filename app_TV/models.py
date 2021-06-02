from django.db import models

# Create your models here.
class Show(models.Model):
     title = models.CharField(max_length=255)
     channel = models.CharField(max_length=255)
     description = models.TextField('')
     release_date = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now = True)

     def __str__(self):
          return f"{self.title}  {self.channel}  {self.id}"