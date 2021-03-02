from django.db import models


class Item(models.Model):
    lists = models.CharField(max_length=255,default=None)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.lists

