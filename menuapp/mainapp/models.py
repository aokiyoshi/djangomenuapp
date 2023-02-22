from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=128)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title